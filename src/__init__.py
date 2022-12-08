import argparse
import sys
sys.path.append("")
import configparser
from fs_crawler import FileSystemCrawler 

# if __name__ == '__main__' checks if a file is imported as a module or not.
# example: 
def main():
#	config = configparser.ConfigParser()
#	config.sections()
#	config.read('example.ini')
#	print(config['DEFAULT']['source'])
	parser = argparse.ArgumentParser(
    	prog='consolidate_subdirectories',
    	description='Will move all files of a type from all subdirectories in source to the root of source, or to dest if provided')

	parser.add_argument('-s', '--source', type=str, default='/')
	parser.add_argument('-d', '--dest', type=str, default='/')
	parser.add_argument('-t', '--type', type=str, default='mp4')
	args = parser.parse_args()

	fs_crawler = FileSystemCrawler(args.source, args.dest, args.type)
	fs_crawler.printt()

def parse_arguments():
	print(sys.argv[1])
      

if __name__ == '__main__':
	main()

   