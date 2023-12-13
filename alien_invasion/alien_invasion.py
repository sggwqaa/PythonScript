from sys import exit
import pygame
class AlienInvasion:
    '''游戏主类,负责实施程序行为并管理游戏资源'''
    def __init__(self):
        '''初始化游戏并创建游戏资源'''
        pygame.init()
        self.screen=pygame.display.set_mode((1200,800))
        pygame.display.set_caption("Alien Invasion")

    def run():
        '''启动游戏主循环'''
        while True:
            for event in pygame.event.get():
                if event.type==pygame.quit:
                    exit()
            pygame.display.flip()

if __name__ == '__main__':
    alien_invasion=AlienInvasion()
    alien_invasion.run()