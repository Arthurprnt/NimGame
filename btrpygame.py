import pygame

class pygameimage():

    def __init__(self, image, pos):
        self.image = image
        self.pos = pos
        self.size = image.get_size()

    def gethitbox(self):
        return (self.pos[0], self.pos[0] + self.size[0], self.pos[1], self.pos[1] + self.size[1])

def collide(image, mouse):
    """
    Check if the mouse cursor collide with an image.
    """
    hitbox = image.gethitbox()
    return hitbox[0] <= mouse[0] <= hitbox[1] and hitbox[2] <= mouse[1] <= hitbox[3]

def showtext(screen, text, font, size, pos, color, align):
    """
    Show text on the screen
    """
    final_font = pygame.font.Font(font, size)
    text_shown = final_font.render(text, True, color)
    text_rect = text_shown.get_rect()
    if align.lower() == "center":
        text_rect.center = pos
    elif align.lower() == "midleft":
        text_rect.midleft = pos
    elif align.lower() == "midright":
        text_rect.midright = pos
    elif align.lower() == "topleft":
        text_rect.topleft = pos
    elif align.lower() == "topright":
        text_rect.topright = pos
    elif align.lower() == "bottomleft":
        text_rect.bottomleft = pos
    else:
        text_rect.bottomright = pos
    screen.blit(text_shown, text_rect)
    return final_font.size(text)

def createbtn(file, size, pos):
    btn = {
        "away": pygameimage(pygame.transform.scale(pygame.image.load(file), size), pos),
        "target": pygameimage(pygame.transform.scale(pygame.image.load(file.replace(".png", "_target.png")), size), pos)
    }
    return btn

def display(screen, btn):
    if not collide(btn['away'], pygame.mouse.get_pos()):
        screen.blit(btn['away'].image, btn['away'].pos)
    else:
        screen.blit(btn['target'].image, btn['target'].pos)