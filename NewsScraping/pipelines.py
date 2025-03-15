# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


import logging
from itemadapter import ItemAdapter
import pymongo

import pymongo
import logging

#mongodb://localhost:27017/
MONGO_URI = "mongodb+srv://jamshidjunaid763:JUNAID12345@insightwirecluster.qz5cz.mongodb.net/?retryWrites=true&w=majority&appName=InsightWireCluster"
DB = 'Scraped-Articles-10'
COLLECTION = 'Articles'

#MONGO_URI = "mongodb://localhost:27017/"
#DB = 'InsightWire'
#COLLECTION = 'Articles'


class AljazeerascraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  

        self.items = []  # List to hold items for bulk insertion
        print("MongoDB connected successfully!")  
            

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item



class ArabnewsscraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  
        
        self.items = []  # List to hold items for bulk insertion

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item
    

class BreitbartscraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  
        
        self.items = []  # List to hold items for bulk insertion

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item
    

class FoxscraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  
        
        self.items = []  # List to hold items for bulk insertion

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item
    
class MeescraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  
        
        self.items = []  # List to hold items for bulk insertion

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item
    
class TimescraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  
        
        self.items = []  # List to hold items for bulk insertion

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item
    

class GuardianscraperPipeline:
    def open_spider(self, spider):
        # Connect to MongoDB
        logging.info("Opening connection to MongoDB")
        self.client = pymongo.MongoClient(MONGO_URI)
        
        self.db = self.client[DB]  # Replace with your database name
        self.collection = self.db[COLLECTION]  # Replace with your collection name

         # Create an index on the 'title' field for faster search (and uniqueness check)
        self.collection.create_index("title", unique=True)  
        
        self.items = []  # List to hold items for bulk insertion

    def close_spider(self, spider):
        # Insert all collected items in bulk
        if self.items:
            try:
                self.collection.insert_many(self.items)
                logging.info(f"Inserted {len(self.items)} items into the collection.")
            except Exception as e:
                logging.error(f"Failed to insert items: {e}")
        
        # Close the connection
        logging.info("Closing connection to MongoDB")
        self.client.close()

    def process_item(self, item, spider):
        try:
            # Check if an article with the same title already exists in the database
            existing_article = self.collection.find_one({"title": item['title']})
            if existing_article:
                logging.info(f"Duplicate article found with title: {item['title']}. Skipping insertion.")
                return None  # Skip processing if it's a duplicate

            # If no duplicate, add item to the list for bulk insertion
            self.items.append(dict(item))
            logging.info(f"Article added to list for insertion: {item['title']}")

        except Exception as e:
            logging.error(f"Failed to process item: {e}")
        
        return item