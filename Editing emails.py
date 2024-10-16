
with open ("Message.txt", "w") as message:
    message.write("Welcome to the party! We hope you can make it. Food fun and friends!")

with open ("Names.txt", "r") as n_file:
    with open ("Message.txt", "r") as m_file:

        body = m_file.read()
        for name in n_file:

            mail = "Hello " + name + body
            with open(name.strip()+".txt", "w") as mailfile:

                mailfile.write(mail)
print("Here's an example of the email created")

with open ("Chris.txt", "r") as chrismail:
    print(chrismail.read())
