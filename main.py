from Post import Post
all_posts_archive = []
user_input = ""
new_post = ""
username = ""

username = input("What would you like your username to be?\n> ")
print(f"\nWelcome, {username}\n")

user_input = input("Choose an option.\nnew\nremove\nchange user\nprint\nquit\n> ")

while user_input != "quit":
    if user_input == "new":
        message = input("\nWhat would you like to say?\n> ").strip()
        new_post = Post(username, message)
        all_posts_archive.append(new_post)
        print(f"\nPost complete.")
    elif user_input == "remove":
        print("\nWhich post would you like to remove?\n")
        for index, post in enumerate(all_posts_archive):
            print(f"Post #: {index}    {post}")
        remove_index = -1
        while remove_index < 0 or remove_index >= len(all_posts_archive):
            remove_index = int(input("\nWhich post would you like to remove?\n> "))
        print(f"\nDeleted {all_posts_archive[remove_index]}")
        del all_posts_archive[remove_index]
    elif user_input == "change user":
        username = input("\nEnter changed username.\n> ").strip()
        print(f"\nUsername has been changed to {username}.\n")
    elif user_input == "print":
        for post in all_posts_archive:
            print(post)
    else:
        print("\nYour selection was invalid.\n")
    user_input = input("\nChoose an option.\nnew\nremove\nchange user\nprint\nquit\n> ")
user_input = ""
