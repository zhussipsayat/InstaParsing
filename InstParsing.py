from instagram import WebAgentAccount, Media

photos = []
agent = WebAgentAccount("zhssp")
agent.auth("cfqufrBcfzrfcfz1997")

medias, pointer = agent.feed()
for media in medias:
    if not media.is_video:
        photos.append(media.display_url)

while not pointer is None:
    medias, pointer = agent.feed(pointer=pointer)
    for media in medias:
        if not media.is_video:
            photos.append(media.display_url)
