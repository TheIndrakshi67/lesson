class ArtGallery:
    def __init__(self, owner_name):
        self.owner = owner_name
        self.artworks = []
        print("Art Gallery initialized for " + self.owner)

    def add_artwork(self, title, artist):
        artwork = {"title": title, "artist": artist}
        self.artworks.append(artwork)
        print("Added: " + title + " by " + artist)

    def display_artworks(self):
        if not self.artworks:
            print("The gallery is currently empty.")
        else:
            print("--- Gallery Collection ---")
            for item in self.artworks:
                print("Title: " + item["title"] + " | Artist: " + item["artist"])

    def __del__(self):
        print("Closing the gallery. All object data deleted.")


def main():
    owner = input("Enter the gallery owner's name: ")
    gallery = ArtGallery(owner)

    while True:
        print("\nMenu:")
        print("1. Add Artwork")
        print("2. Display Collection")
        print("3. Exit Program")
        
        choice = input("Enter your choice (1-3): ")

        if choice == "1":
            title = input("Enter artwork title: ")
            artist = input("Enter artist name: ")
            gallery.add_artwork(title, artist)
        elif choice == "2":
            gallery.display_artworks()
        elif choice == "3":
            print("Exiting menu loop...")
            break
        else:
            print("Invalid choice. Please try again.")

    del gallery


main()
