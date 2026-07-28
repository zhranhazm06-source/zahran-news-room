from news_sources import NEWS_SOURCES

print("=" * 50)
print("ZAHRAN NEWS ROOM")
print("Egypt Real Estate News Monitor")
print("=" * 50)

def main():
    print("Monitoring official news sources...")
    print()

    for source in NEWS_SOURCES:
        print(f"✓ {source['name']}")
        print(f"  {source['url']}")
        print()

if __name__ == "__main__":
    main()
