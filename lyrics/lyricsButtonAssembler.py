import os
import sys

def printColumns(cols, file):
    file.write("""<div class="songListContainer container">
          <div class="row">\n\n""")
    for column in cols[1::]:
        file.write("""            <span class="border-right">
            <div class="col-auto">
              <h3>""" + column[0] + """</h3>""" + """<small>""" + str(len(column[1])) + """ Songs</small>""" + """<br>\n""")
        for song in column[1]:
              file.write("""\n              <button class="btn orange-btn" onclick='fillSegmentWithLyrics("slavic/"""
              + column[0] + "/" + song + """")'>""" + song + """</button>
              <br>\n""")

        file.write("""            </div>
          </span>\n\n""")
    file.write("""          </div>
        </div>\n""")
              
        
def doSlavic(f):
    path = "txt/slavic/"
    cols = []

    for (root, directories, files) in os.walk(path):
        # Grabbing artist's name
        artist = root.split("/")[2]
        
        #print(artist)
        #print("New Column", artist)

        # Building song repotoire
        songs = []
        for file in files:
            songs.append(file)
            #print("\t\t", file)

        # Finishing up data structure for this artist and printing it:
        cols.append((artist, songs))

    #input()
    printColumns(cols, f)

#doSlavic()

"""
# Walk through the /txt/slavic folder
list_of_files = {}
walked = os.walk(path)

print(walked)

for (root, directories, files) in walked:
    for directory in directories:
        print(directory)
    print("\n\n")
    for file in files:
        print(file)
    print("\n\n")
   #print(dirpath, dirnames, filenames, "\n\n")
    #for filename in filenames:
     #   if filename.endswith('.txt'): 
      #      list_of_files[filename] = os.sep.join([dirpath, filename])
      """
# Walk through the subfolders of artists
# Each artist becomes their own column (alpha order)

# Each txt gets turned into a button 

# Any files in the root /txt/slavic folder are pushed to the last column

# Print out the final HTML result :) 


# TODO: See if the columns, if for instance one
# is like 10 items and another is 3 items, play nicely together.
# Otherwise, I may have to make some special maths for each one or a dumb way
# of counting how many songs each artist has to make the most balanced column
# arrangement. Or I may have to make it so that the sections are collapsed
# by default. 
