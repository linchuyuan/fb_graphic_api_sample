# QUESTIONS
  # There are 3 class methods, each with an output task for you to complete
# NOTES
  # We have created a dummy user account for you to query
  # Please use the declared access_token and user_id for your queries. Do not change these values.
# HELPFUL REFERENCES
  # For the FB User API, see https://developers.facebook.com/docs/graph-api/reference/user/
  # For the complete FB Reference Guide, see https://developers.facebook.com/docs/graph-api/reference
  # For a helpful FB API Explorer, you can register and use https://developers.facebook.com/tools/explorer/

import json
import requests

ACCESS_TOKEN = "EAAWJaOclG7kBAAOfGKZC9PZBfCIfsyAx3j6K1NOBKdTUW1HwTb97oO5S8KZCnQNxGZCZCWu2frEj1X9Jyfv0EGxXUpwUOgJQF2brTZBE2Yaew62UJ9SOXPkZCHVQqRMUzo9G6wsx1p5ayduWO7ZAxbrkok5zwdF1E2cZD"
# Token expires July 23rd, 2016
USER_ID = "me"  


class FbGrapy:
	def __init__ (self):
		self.USER_ID = "me";
		self.url = "https://graph.facebook.com/v2.6/";
	
	def about_me(self):
		self.body = {
                        'access_token': ACCESS_TOKEN,
                        'fields': "id,name,birthday,education,languages",
                	}
		r = requests.get(self.url + self.USER_ID, params=self.body)
		output = json.loads(r.text)
		# TASK 1: Update the output to include the languages I speak, my birthday, and where I went to school
		return_me = {};
		return_me["name"] = output["name"];
		return_me["school"] = [];
		for i in range(len(output["education"])):
			return_me["school"].append(output["education"][i]["school"]["name"]);

		return_me["birthday"] = output["birthday"];
		return_me["languages"] = [];
		for i in range(len(output["languages"])):
                        return_me["languages"].append(output["languages"][i]["name"]);
		print "--------------------------------Task #1 My Info--------------------------------------";
		print "Name: " + (str(return_me["name"]));
		print "School: " , 
		for i in range(len(return_me["school"])): print return_me["school"][i],
		print "";
		print "Birthday: " + (str(return_me["birthday"]));
		print "Languages: " ,
                for i in range(len(return_me["languages"])): print return_me["languages"][i],
		print "";

		return return_me;
	

	def my_albums(self,print_indicator = True):
		self.body = {
                        'access_token': ACCESS_TOKEN,
			'fields':'id,count,name'
                	}
		r = requests.get("https://graph.facebook.com/v2.6/" + self.USER_ID + "/albums", params=self.body)
                output = json.loads(r.text)
		return_me = output["data"];
		if print_indicator:
			print "--------------------------------Task #2 My Albums------------------------------------";
			for i in range(len(return_me)):
				print "name: " + str(return_me[i]["name"]);
				print "id: " + str(return_me[i]["id"]);
				print "Photo Count: " + str(return_me[i]["count"]);
				print "**";
		return return_me


	def all_albums_photos(self):
		# TASK 3:
			# Step 1. Call my_albums from the previous task to get a list of all my album ids
			# Step 2. output all captions of every photo for each album id
		my_albums_info = self.my_albums(print_indicator=False);
	        self.body = {
                        'access_token': ACCESS_TOKEN,
                        'fields':'description,name'
                        }
		id_list = [];
		album_list = [];
		return_me = {};
		for i in range(len(my_albums_info)):
			id_list.append(my_albums_info[i]["id"]);
			album_list.append(my_albums_info[i]["name"]);
		print "------------------------------Task #3 Photo Detail-----------------------------------";
		for i in range(len(id_list)):
			url = self.url + id_list[i] + "/photos/?limit=500";
			r = requests.get(url, params=self.body);
			output = json.loads(r.text);
			output = output["data"];
			return_me[album_list[i]] = [];
			print "album - " + album_list[i];
			for k in range(len(output)):
				try:
					print "\t Caption: " + output[k]["name"];
					return_me[album_list[i]].append(output[k]["name"]);
				except:
					print "\t photo id->" + output[k]["id"] + ": !!no caption found for this id";
					return_me[album_list[i]].append(output[k]["id"] + " no caption");
		return return_me;


def main ():
	fb = FbGrapy();
	fb.about_me();
	fb.my_albums();
	fb.all_albums_photos();

if __name__ == '__main__':
        main();

