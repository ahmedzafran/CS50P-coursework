# Knitting shirts with code
    #### Video Demo:
     https://youtu.be/MTl3UgAhtD0
    #### Description:
    The program functions as a shirt design model, which shows you how your custom order of an embroided or stitched shirt will look with any two characters. It allows you to design a shirt based of your own custom choices with certain limitations and extra charges. The prices and extra charges are tracked using a object oriented system which is stored dynamically. The complexity of this program includes the use of an object oriented system, the cohesion of integrating seperate functioning libraries, not intended by default, to create a new use-case altogether. The design of the stitching of characters on the shirt uses ASCII art from a library, called, "art", carefully considered to mimic the stitching of initials on a shirt. The shirt itself is the original shirt template from the problem set "Shirtificate". This is used instead of other shirt templates online, to ensure that the image is always avaialble relevant to course facillities. However instead of using a "wget <url>" command in terminal to locally and manually retrieve the shirt, a "get" request is sent programmatically to ensure anyone running the program can retrieve the required asset. "fpdf2" is used to merged the shirt and the ASCII art, creating a model of the user's custom inputs and design preferences, along with a print of the final price. Other than the methods stated above, the program also uses many techniques taught throughout the course which includes but not limited to, loops, conditionals, libraries, Object-Oriented Programming, API requests and unit testing.

    Some Design considerations or limitations of the project include, the use of Artificial Intelligence (AI), initially, it was desired to
    use an Large-Language Model, prompt system to generate ASCII art for shirt prints, based of the user's input. However this is was not
    plausible due to pay walls, with API keys and potential GPU or infrastructure requirements of the project, which exceed more than just a basic locally run script. Not being aware of potential infrastructure resource available to the students through the use of "CS50.dev". Considering such potential issues, it was deviced to fall back to simpler ASCII art libraries to do the shirt prints and to still demonstrate possible complexities of the project in similar fashion.

    The program presents a basic shirt which can be bought for 15$ however if you wish to add an embroided or stitched design
    of any two characters you may at an extra cost of 5$ per character added. The user may then select a color for the thread used to
    stitch their design, however that also comes at an extra cost, differing based on the color chosen by the user. Finally the user receives a recipt in terminal, displaying the user's decisions for the shirt design, in "print characters", the color of the thread for the stitch and, the total overall cost of the shirt considering the custom choices the user has made. Finally, a ".pdf" file is released, for the user to view, showing the shirt made with the design considerations of the user. This is to mimic a modelling of ordering a custom shirt online, and being able to view your designed shirt, before it is shipped to you, along with the order recieupt of your order, encompassing the cost of your custom design considerations, and further details.


    TODO
1. install the dependencies listed in the requirements.txt with "pip install <library>"
1. run the program with "python project.py"
2. enter up to any 2 characters to have it customly knitted onto a shirt with the final price in mind
3. select the color of your thread by entering a number from the prompt with the final price in mind
4. open custom_order.pdf to view your shirts design, and the receipt of your custom order on the second page.
