import math
import threading
from person import person
from account import account
from experience import experience

def clear_screen():
    for _ in range(40):
        print()

def get_valid_input(valid_inputs = None, message = ""):
    clear_screen()
    user_input = input(message).strip()
    try: 
        user_input = int(user_input)
    except ValueError:
        pass
    if not valid_inputs:
        return user_input
    if user_input in valid_inputs:
        return user_input
    return get_valid_input(valid_inputs, message)

class cliservice(object):
    def __init__(self):
        self.logged_in = False
        self.signed_in_acc = None
        self.state = 0
        account.load_metadata()

    def sign_up(self, username, password):
        user = person()
        acc = account(user, username, password)
        self.signed_in_acc = acc
        self.state = 1

    def login(self, username, password): # TODO: load information instead of doing the samething as sign up
        user = person()
        acc = account(user, username, password)
        self.signed_in_acc = acc
        self.state = 1

    def log_out(self):
        self.signed_in_acc.to_json()
        self.signed_in_acc = None

    def set_state(self, state):
        self.state = state

    def homepage(self):
        msg = """
        Homepage
        (1) - Manage profile
        (2) - Manage experiences
        (3) - Account settings
        ----------------------------------------------------------------
        (9) - Log out
        """
        response = get_valid_input([1, 2, 3, 9], msg)
        return response

    def profile_page(self):
        msg = f"""
        Profile
        Email address: {self.signed_in_acc.get_email()}
        Address: {self.signed_in_acc.get_address()}
        (1) - Update Email
        (2) - Update Address
        ----------------------------------------------------------------
        (9) - Back
        """
        response = get_valid_input([1, 2, 9], msg)
        return response

    def experience_page(self):
        msg = """
        Experiences
        (1) - Add an experience
        (2) - Show list of experiences 
        ----------------------------------------------------------------
        (9) - Back
        """
        response = get_valid_input([1, 2, 9], msg)
        return response

    def account_setting_page(self):
        msg = """
        Account Settings
        (1) - Change username
        (2) - Update password
        ----------------------------------------------------------------
        (9) - Back
        """
        response = get_valid_input([1, 2, 9], msg)
        return response

    def add_experience_page(self):
        type = get_valid_input(["W", "V", "E", "S"], "Select a Type: (W)ork, (V)olunteer, (E)ducation, (S)kills")
        title = input("Title:")
        description = input("Description:")
        return experience(type, title, description)
        # start = input("Start date: (mm/yy)")
        # end = input("End date: (mm/yy)")

    def experience_list_page(self):
        experiences = [exp.get_title() for exp in self.signed_in_acc.experiences]
        self.current_page = 1
        self.num_of_pages = math.ceil(len(experiences) / 6)
        if len(experiences) > 0:
            matrix = self.signed_in_acc.get_experiences(6)
        else:
            matrix = [experience("Work", "None") for _ in range(6)]
        

        msg = f"""
        List of Experiences (Select to view)
        (1) - {matrix[self.current_page-1][0].get_titles()}
        (2) - {matrix[self.current_page-1][1].get_titles()}
        (3) - {matrix[self.current_page-1][2].get_titles()}
        (4) - {matrix[self.current_page-1][3].get_titles()}
        (5) - {matrix[self.current_page-1][4].get_titles()}
        (6) - {matrix[self.current_page-1][5].get_titles()}
        
        ------------------------------------------------------------- {self.current_page}/{self.num_of_pages}
        (7) - Previous Page
        (8) - Next Page
        (9) - Back
        """
        response = get_valid_input([1, 2, 3, 4, 5, 6, 7, 8, 9], msg)
        return response

    def next_page(self):
        if self.current_page and self.num_of_pages:
            if self.current_page + 1 <= self.num_of_pages:
                self.current_page += 1

    def previous_page(self):
        if self.current_page and self.num_of_pages:
            if self.current_page - 1 > 0:
                self.current_page -= 1
        

    def update_experience_page(self, experien):
        pass
        # start = input("Start date: (mm/yy)")
        # end = input("End date: (mm/yy)")


if __name__ == '__main__':
    LOGIN = 0
    HOMEPAGE = 1
    PROFILE_PAGE = 2
    EXPERIENCE_PAGE = 3
    ACCOUNT_SETTINGS = 4


    run = True
    cli = cliservice()
    while run:

        if cli.state == LOGIN: # No user signed in
            response = get_valid_input(valid_inputs=["L", "S", "Q"], message="Welcome to auto resume\n(L)ogin/(S)ign up/(Q)uit")
            if response == "S":
                cli.sign_up(get_valid_input(message="Enter a username: "), get_valid_input(message="Enter a password: "))
            elif response == "L":
                cli.login(get_valid_input(message="Enter a username: "), get_valid_input(message="Enter a password: "))
            elif response == "Q":
                run = False
                account.save_metadata()
                print("bye")

        elif cli.state == HOMEPAGE: # Homepage 
            response = cli.homepage()
            if response == 1: # GO to profile page
                cli.set_state(PROFILE_PAGE)
            elif response == 2: # Go to experience page
                cli.set_state(EXPERIENCE_PAGE)
            elif response == 3: # Go to accounts page
                cli.set_state(ACCOUNT_SETTINGS)
            elif response == 9: # Logout
                cli.log_out()
                cli.set_state(LOGIN)

        elif cli.state == PROFILE_PAGE: # Profile page
            response = cli.profile_page()
            if response == 1:
                clear_screen()
                cli.signed_in_acc.update_email(input("Email:"))
            elif response == 2:
                clear_screen()
                cli.signed_in_acc.update_address(input("Address:"))
            elif response == 9: # Go back to home page
                cli.set_state(HOMEPAGE)

        elif cli.state == EXPERIENCE_PAGE: # Experience page
            response = cli.experience_page()
            if response == 1:
                cli.signed_in_acc.add_experience(cli.add_experience_page())
            elif response == 2:
                exp_rspn = cli.experience_list_page() # TODO: implement showing list of experiences
                if exp_rspn == 7:
                    cli.previous_page()
                elif exp_rspn == 8:
                    cli.next_page()
                elif exp_rspn == 9:
                    cli.set_state(EXPERIENCE_PAGE)
                
            elif response == 9:  # Go back home page
                cli.set_state(HOMEPAGE)
                
        elif cli.state == ACCOUNT_SETTINGS: # Account settings page
            response = cli.account_setting_page()
            if response == 1: # Update username
                pass # TODO: implement updating username
            if response == 2: # Update password
                pass # TODO: implement updating password
            if response == 9: # Go back to home page   
                cli.set_state(HOMEPAGE)


    
    
    
    
        

