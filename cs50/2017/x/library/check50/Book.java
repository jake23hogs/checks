public class Book {

    private String title, author;

// This is the constructor. Notice same name as the class and it is giving
// initial values to title and author.
    public Book(String t, String a) {
        title = t;
        author = a;
    }

    public String getAuthor() {
        return author;
    }

    public String getTitle() {
        return title;
    }

    public String toString() {
        return "Title:   " + title + "\n"
                + "Author:  " + author;
    }
}