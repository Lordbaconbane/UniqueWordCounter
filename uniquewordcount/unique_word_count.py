import re

def unique_word_count():
    wordDict = {}
    with open("check_file.txt", "r", encoding='utf-8') as f:
        lines = f.read()
        lines = lines.lower()
        print("--------------")
        # Blacklist words
        with open("blacklist.txt", "r") as b:
            for word in b:
                # Set words to lower case and remove leading white space/spaces
                word = word.lower()
                word = word.strip()
                # Use Reg expressions to catch whole words
                pattern = r'\b' + re.escape(word) + r'\b'
                lines = re.sub(pattern, '', lines)
                # Remove any extra spaces left behind after removal
                lines = re.sub(r'\s+', ' ', lines).strip()
        lines = lines.split()
        for element in lines:
            if element in wordDict:
                pass
            else:
                count = lines.count(element)
                wordDict.update({element:count})
        sortedDict = dict(sorted(wordDict.items(), key=lambda item: item[1], reverse=True))
        
        with open("output.txt","w", encoding='utf-8') as o:
            for key, value in sortedDict.items():
                o.write(f"{key}: {value}\n")
    return sortedDict

unique_word_count()