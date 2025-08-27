class HTMLPageGenerator:
    def __init__(self):
        self.name = None
        self.title = None
        self.heading = None
        self.description = None

    def get_name(self):
        """Get user name"""
        while True:
            try:
                self.name = input("Enter your name: ")
                if not self.name.strip():
                    print("Name cannot be empty.")
                else:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_title(self):
        """Get webpage title"""
        while True:
            try:
                self.title = input("Enter your webpage title: ")
                if not self.title.strip():
                    print("Title cannot be empty.")
                else:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_heading(self):
        """Get heading for the webpage"""
        while True:
            try:
                self.heading = input("Enter your webpage heading: ")
                if not self.heading.strip():
                    print("Heading cannot be empty.")
                else:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def get_description(self):
        """Get description for the webpage"""
        while True:
            try:
                self.description = input("Enter your webpage description: ")
                if not self.description.strip():
                    print("Description cannot be empty.")
                else:
                    break
            except Exception as e:
                print(f"An error occurred: {e}")

    def generate_html(self):
        """Generate HTML page"""
        html = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>{self.title}</title>
</head>
<body>
<h1>{self.heading}</h1>
<p>Welcome, {self.name}!</p>
<p>{self.description}</p>
</body>
</html>"""
        return html

def main():
    generator = HTMLPageGenerator()
    
    print("Welcome to the HTML Page Generator!")
    input("Press Enter to continue...")
    
    print("\nPlease enter the following information:")
    
    generator.get_name()
    generator.get_title()
    generator.get_heading()
    generator.get_description()
    
    html = generator.generate_html()
    print("\nHere's your generated HTML code:")
    print(html)
    
if __name__ == "__main__":
    main()
