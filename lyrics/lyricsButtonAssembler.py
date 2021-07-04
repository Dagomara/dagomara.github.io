import os
import sys

# cols structure is [.., [author 1, [songs]], ...]

# Sorts artists by how many songs of theirs I have in the system, ascending. 
def sortArtistsBySongCount(cols):
    newCols = []
    for column in cols:
        newCols.append(column)
    #print(cols, "\n", newCols)
    #input()
    newCols.sort(key=lambda x: len(x[1]))
    #print(newCols)
    return newCols

# Does a bunch of HTML work for each artist in cols given. 
def processArtists(cols, file):
    file.write("""<div class="songListContainer container">
          <div class="row">\n\n""")

    # For each artist:
    for column in cols:
        # Setting up column header w/ artist information
        authorFirstName = column[0].split(" ")[0] # used for div id
        file.write("""            <span class="border-right">
            <div class="col-auto">
              <a href="#""" + authorFirstName + "\"" + """ data-toggle="collapse"><h3>"""
                   + column[0] + """</h3></a>""" + """<small>"""
                   + str(len(column[1])) + """ Songs</small>""" + """<br>\n<div id=""" + "\""
                   + authorFirstName + "\"" + """ class="collapse">""")

        # Building the list of individual songs
        for song in column[1]:
              file.write("""\n              <button class="btn orange-btn" onclick='fillSegmentWithLyrics("slavic/"""
              + column[0] + "/" + song + """")'>""" + song + """</button>
              <br>\n""")

        # Tidying up loose ends
        file.write("""            </div></div>
          </span>\n\n""")
    file.write("""          </div>
        </div>\n""")
              
# Runs through the slavic folder and puts all artist/song information in html file f.
def doSlavic(f):
    path = "txt/slavic/"
    cols = []

    # For each artist:
    for (root, directories, files) in os.walk(path):
        # Grabbing artist's name
        artist = root.split("/")[2]
        
        #print(artist)
        #print("New Column", artist)

        # Building song repotoire of artist in question
        songs = []
        for file in files:
            songs.append(file)
            #print("\t\t", file)

        # Finishing up data structure for this artist
        cols.append((artist, songs))
        
    # Chopping off junk entry at the beginning of cols
    cols = cols[1::]

    # Now that the artists have been arranged into a python-handleable format,
    # put them into the HTML file :)
    processArtists(sortArtistsBySongCount(cols), f)

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
