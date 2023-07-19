import PyPDF2
import re
def check_valid_filename(filename):
    invalid_chars = r'[/\\:*?"<>|]'
    if not re.search(invalid_chars, filename):
        return True
    print('A file name cannot contain any of these characters / \\ : * ? " < > |')
    return False

# Note: here instead of Python.pdf you should give the whole path to the pdf if the pdf is not present in the same directory where python program is present
with open('Python.pdf', mode='rb') as merged_pdf:
    pdf = PyPDF2.PdfFileReader(merged_pdf)

    (u, ctr, x) = tuple([0]*3)
    for _ in range(1, pdf.numPages+1):
        if u >= pdf.numPages:
            print("Successfully done!")
            exit(0)

        while True:
            name = input("Enter the name of the pdf: ")
            if check_valid_filename(name) == True:
                break

        while True:
            ctr = input(f"Enter the number of pages for {name}: ")
            try:
                ctr = int(ctr)
                if ctr > 0:
                    break
                else:
                    raise ValueError
            except ValueError:
                print("Page number must be a positive integer")

        u += ctr
        if u > pdf.numPages:
            print('Limit exceeded! ')
            break

        # Note: In the braces you should give the desired path of where new files should be stored
        base_path = '{}.pdf'
        # If you want to store the new pdfs in the same directory, then leave the braces empty
        path = base_path.format(name)
        with open(path, mode='wb') as f:
            pdf_writer = PyPDF2.PdfFileWriter()

            for j in range(x, x+ctr):
                page = pdf.getPage(j)
                pdf_writer.addPage(page)

            x += ctr

            pdf_writer.write(f)
print("Successfully done!")
