import re

def get_matching_words(regex):
    words = ["aimlessness", "assassin", "baby", "beekeeper", "belladonna", "cannonball", "crybaby", "denver", "embraceable", "facetious", "flashbulb", "gaslight", "hobgoblin", "iconoclast", "issue", "kebab", "kilo", "laundered", "mattress", "millennia", "natural", "obsessive", "paranoia", "queen", "rabble", "reabsorb", "sacrilegious", "schoolroom", "tabby", "tabloid", "unbearable", "union", "videotape"]
    matches = []
    for word in words:
        if re.search(regex,word):
            matches.append(word)
    return matches

print 'These words have a v:',get_matching_words(r'v')
print 'These words have a double-s:',get_matching_words(r'ss')
print 'These words end in e:',get_matching_words(r'e$')
print 'These words contain a b any character and then another b:',get_matching_words(r'b.b')
print 'These words containt b, any number of characters, then another b:',get_matching_words(r'b*b')
# print 'These words include all five vowels in order:',get_matching_words()
# print 'These words use the letters in "regular expression":',get_matching_words()
print 'These words contain a double letter:',get_matching_words(r'..')
