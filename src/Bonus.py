import Resources


class Bonus:
    def __init__(self, px, py, bonus_num, world):
        self.world = world
        self.world.objects.append(self)
        self.type = 'bonus'

        self.image = Resources.imgBonuses[bonus_num]
        self.rect = self.image.get_rect(center = (px, py))

        self.timer = 600
        self.bonusNum = bonus_num

    def update(self):
        if self.timer > 0:
            self.timer -= 1

        else:
            self.world.objects.remove(self)

        for obj in self.world.objects:
            if obj.type == 'tank' and self.rect.colliderect(obj.rect):
                if self.bonusNum == 0:
                    if obj.rank < len(Resources.imgTanks) - 1:
                        obj.rank += 1
                        self.world.objects.remove(self)
                        break
                elif self.bonusNum == 1:
                    obj.hp += 1
                    self.world.objects.remove(self)
                    break

    def draw(self, window):
        window.blit(self.image, self.rect)
