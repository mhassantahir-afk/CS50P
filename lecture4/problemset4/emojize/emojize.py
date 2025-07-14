import emoji

em = (input("input:"))

em = emoji.emojize(em)
em = emoji.emojize(em, language="alias")


print(em)
