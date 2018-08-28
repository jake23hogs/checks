// Solution to Project 6.6
// Represents a patron with a name and up to three books

public class Patron {

    private String name;
    private Book book1, book2, book3;

    public Patron(String n) {
        name = n;
        book1 = null;
        book2 = null;
        book3 = null;
    }

    public String getName() {
        return name;
    }

    public boolean borrowBook(Book b) {
        if (book1 == null) {
            book1 = b;
            return true;
        } else if (book2 == null) {
            book2 = b;
            return true;
        } else if (book3 == null) {
            book3 = b;
            return true;
        } else {
            return false;
        }
    }

    public boolean returnBook(String title) {
        if (book1 != null) {
            if (book1.getTitle().equals(title)) {
                book1 = null;
                return true;
            }
        }
        if (book2 != null) {
            if (book2.getTitle().equals(title)) {
                book2 = null;
                return true;
            }
        }
        if (book3 != null) {
            if (book3.getTitle().equals(title)) {
                book3 = null;
                return true;
            }
        }
        return false;
    }

    public boolean hasBook(String title) {
        if (book1 != null) {
            if (book1.getTitle().equals(title)) {
                return true;
            }
        }
        if (book2 != null) {
            if (book2.getTitle().equals(title)) {
                return true;
            }
        }
        if (book3 != null) {
            if (book3.getTitle().equals(title)) {
                return true;
            }
        }
        return false;
    }

    public String toString() {
        String str = "Patron's name:  " + name;
        if (book1 != null) {
            str = str + "\n" + book1;
        }
        if (book2 != null) {
            str = str + "\n" + book2;
        }
        if (book3 != null) {
            str = str + "\n" + book3;
        }
        return str;
    }
}