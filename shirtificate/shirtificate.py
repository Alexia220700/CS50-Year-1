# Import required libraries
from fpdf import FPDF  # For PDF generation
import sys  # For system exit and error handling

def main():
    """
    Main function to generate a customized CS50 shirtificate PDF.
    Handles user input, PDF creation, and error management.
    Returns 0 on success, 1 on failure.
    """
    try:
        # USER INPUT SECTION 
        # Prompt user for their name and validate input
        name = input("Enter your name: ").strip()
        if not name:
            raise ValueError("Name cannot be empty")

        #  PDF INITIALIZATION
        # Create PDF document with A4 portrait orientation
        pdf = FPDF(orientation="portrait", format="A4")
        pdf.add_page()  # Add the first (and only) page

        # Configure PDF to prevent automatic page breaks
        pdf.set_auto_page_break(False, margin=0)

        #  TITLE SECTION
        # Set font for the title and add centered text
        pdf.set_font("Helvetica", "B", 36)  # Bold Helvetica, size 36
        pdf.cell(0, 40, "CS50 Shirtificate", align="C", new_x="LMARGIN", new_y="NEXT")

        # IMAGE PLACEMENT
        # Calculate center position for the shirt image (A4 width = 210mm)
        image_width = 160  # Width of the shirt image in mm
        x_position = (210 - image_width) / 2  # Center calculation

        # Add the shirt image to the PDF with error handling
        try:
            # Place image 80mm from top, centered horizontally
            pdf.image("shirtificate.png", x=x_position, y=80, w=image_width)
        except RuntimeError as e:
            # Convert library error to more descriptive error
            raise FileNotFoundError("Could not find shirtificate.png") from e

        # NAME PLACEMENT ON SHIRT
        # Configure text settings for the name
        pdf.set_font("Helvetica", "B", 24)  # Bold Helvetica, size 24
        pdf.set_text_color(255, 255, 255)  # Set text color to white (RGB)

        # Calculate centered position for the name text
        text_width = pdf.get_string_width(name)  # Get rendered width of name
        text_x = (210 - text_width) / 2  # Center calculation
        pdf.text(x=text_x, y=140, txt=name)  # Place text at calculated position

        # OUTPUT GENERATION
        # Save the PDF file
        pdf.output("shirtificate.pdf")
        print("Successfully created shirtificate.pdf")
        return 0  # Return success code

    except Exception as e:
        # Handle any errors that occur during execution
        print(f"Error: {e}", file=sys.stderr)  # Print to stderr
        return 1  # Return error code

if __name__ == "__main__":
    # Execute main function and exit with proper status code
    sys.exit(main())
