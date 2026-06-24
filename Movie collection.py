def show_menu():
    print("1. Add movie")
    print("2. Show movies")
    print("3. Search movie")
    print("4. Delete movie")
    print("5. Show movie by general")
    print("6. Exit")
def Add_movie(name,genre,rating):
    file=open("movie.txt", "a")
    file.write(name+","+genre+","+rating+"\n")
    file.close()
    return "Movie Added"
def show_movies():
    file=open("movie.txt","r")
    content=file.read()
    file.close()
    return content
def search_movie(name):
    file=open("movie.txt", "r")
    content=file.read()
    file.close()
    if name in content:
        return content
    else:
        return "Not found"
def Delete_movie(name):
    file=open("movie.txt","r")
    lines=file.readlines()
    file.close()
    file=open("movie.txt","w")
    for line in lines:
        parts=line.strip().split(",")
        movie_name=parts[0]
        if movie_name !=name:
            file.write(line)
    file.close()
    return "movie deleted"
def show_movies_by_genre(typ):
    file=open("movie.txt", "r")
    lines=file.readlines()
    file.close()
    result=""
    for line in lines:
        parts=line.strip().split(",")
        genre=parts[1]
        if genre ==typ:
            result=result+line
    return result
operations={
    "1": Add_movie,
    "2": show_movies,
    "3": search_movie,
    "4": Delete_movie,
    "5": show_movies_by_genre
}
def main():
    while True:
        show_menu()
        choice=input("Choose: ")
        if choice=="6":
            print("Goodbye")
            break
        if choice not in operations:
            print("Invalid choice")
            continue
        if choice=="1":
            name=input("Enter name: ")
            genre=input("Entre Genre: ")
            rating=input("Enter rating: ")
            result=operations[choice](name,genre,rating)
            print(result)
        elif choice=="2":
            result=operations[choice]()
            print(result)
        elif choice=="3":
            name=input("Enter name: ")
            result=operations[choice](name)
            print(result)
        elif choice=="4":
            name=input("Enter name: ")
            result=operations[choice](name)
            print(result)
        elif choice=="5":
            typ=input("Enter typ: ")
            result=operations[choice](typ)
            print(result)
main()
