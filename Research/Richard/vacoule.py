import pygame
import random
import math
import sys
from pygame.locals import *

pygame.init()


WIDTH, HEIGHT = 1000, 700
FPS = 60
BACKGROUND = (240, 248, 255)  
PARAMECIUM_COLOR = (100, 200, 150)
YEAST_COLOR = (255, 255, 200)
VACUOLE_COLOR = (255, 200, 150)
CILIA_COLOR = (200, 230, 200)
ORAL_GROOVE_COLOR = (150, 180, 130)
CONTROL_PANEL_COLOR = (220, 220, 220)
BUTTON_COLOR = (180, 180, 180)
BUTTON_HOVER_COLOR = (200, 200, 200)


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Enhanced Paramecium Food Vacuole Formation Simulator")
clock = pygame.time.Clock()

class Button:
    def __init__(self, x, y, width, height, text, action=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.action = action
        self.is_hovered = False
        self.font = pygame.font.SysFont('Arial', 16)
        
    def draw(self, surface):
        color = BUTTON_HOVER_COLOR if self.is_hovered else BUTTON_COLOR
        pygame.draw.rect(surface, color, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        
        text_surf = self.font.render(self.text, True, (0, 0, 0))
        text_rect = text_surf.get_rect(center=self.rect.center)
        surface.blit(text_surf, text_rect)
        
    def check_hover(self, pos):
        self.is_hovered = self.rect.collidepoint(pos)
        return self.is_hovered
        
    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1 and self.is_hovered:
            if self.action:
                self.action()

class Slider:
    def __init__(self, x, y, width, height, min_val, max_val, initial_val, label):
        self.rect = pygame.Rect(x, y, width, height)
        self.min = min_val
        self.max = max_val
        self.value = initial_val
        self.label = label
        self.handle_rect = pygame.Rect(x + (initial_val - min_val)/(max_val - min_val) * (width - 20), 
                                      y, 20, height)
        self.dragging = False
        self.font = pygame.font.SysFont('Arial', 14)
        
    def draw(self, surface):
        
        pygame.draw.rect(surface, (200, 200, 200), self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 1)
        
        
        pygame.draw.rect(surface, (100, 100, 255) if self.dragging else (150, 150, 255), self.handle_rect)
        pygame.draw.rect(surface, (0, 0, 0), self.handle_rect, 1)
        
        
        label_surf = self.font.render(f"{self.label}: {self.value:.1f}", True, (0, 0, 0))
        surface.blit(label_surf, (self.rect.x, self.rect.y - 20))
        
    def update(self):
        if self.dragging:
            mouse_x = pygame.mouse.get_pos()[0]
            new_x = max(self.rect.x, min(mouse_x, self.rect.x + self.rect.width - 20))
            self.handle_rect.x = new_x
            self.value = self.min + (new_x - self.rect.x) / (self.rect.width - 20) * (self.max - self.min)
            
    def handle_event(self, event):
        if event.type == MOUSEBUTTONDOWN and event.button == 1:
            if self.handle_rect.collidepoint(event.pos):
                self.dragging = True
        elif event.type == MOUSEBUTTONUP and event.button == 1:
            self.dragging = False

class YeastParticle:
    def __init__(self, speed_factor=1.0):
        self.radius = random.randint(4, 10)
        self.x = random.randint(WIDTH, WIDTH + 100)
        self.y = random.randint(50, HEIGHT - 50)
        self.base_speed = random.uniform(0.5, 1.5)
        self.speed_factor = speed_factor
        self.engulfed = False
        self.digestion = 0  
        self.in_oral_groove = False
        self.angle = random.uniform(0, 2 * math.pi)
        self.rotation = 0
        self.pulse = 0
        self.pulse_speed = random.uniform(0.05, 0.1)
        
    @property
    def speed(self):
        return self.base_speed * self.speed_factor
        
    def update(self):
        if not self.engulfed:
            
            self.angle += random.uniform(-0.2, 0.2)
            self.x -= self.speed
            self.y += math.sin(self.angle) * 0.5
            
           
            self.rotation += 0.02
            
            
            self.pulse += self.pulse_speed
            
            
            if self.x < -20:
                self.x = WIDTH + 20
                self.y = random.randint(50, HEIGHT - 50)
        else:
            
            self.digestion += 0.1
            if self.digestion > 100:
                self.digestion = 100
    
    def draw(self, surface):
        pulse_offset = math.sin(self.pulse) * 2
        
        if not self.engulfed:
            
            yeast_rect = pygame.Rect(int(self.x - self.radius), int(self.y - self.radius), 
                                   self.radius*2, self.radius*2)
            
            
            pygame.draw.ellipse(surface, YEAST_COLOR, yeast_rect)
            pygame.draw.ellipse(surface, (200, 200, 150), yeast_rect, 1)  
            
            
            nucleus_radius = self.radius // 2
            nucleus_x = self.x + math.cos(self.rotation) * (self.radius - nucleus_radius - 1)
            nucleus_y = self.y + math.sin(self.rotation) * (self.radius - nucleus_radius - 1)
            pygame.draw.circle(surface, (220, 220, 150), (int(nucleus_x), int(nucleus_y)), nucleus_radius)
            
            
            if random.random() > 0.7:  
                scar_x = self.x - math.cos(self.rotation) * (self.radius - 2)
                scar_y = self.y - math.sin(self.rotation) * (self.radius - 2)
                pygame.draw.circle(surface, (180, 180, 130), (int(scar_x), int(scar_y)), 2)
        else:
           
            color = (
                min(255, VACUOLE_COLOR[0] + self.digestion),
                max(0, VACUOLE_COLOR[1] - self.digestion),
                max(0, VACUOLE_COLOR[2] - self.digestion//2)
            )
            
            
            digestion_radius = self.radius + pulse_offset * (self.digestion / 100)
            pygame.draw.circle(surface, color, (int(self.x), int(self.y)), int(digestion_radius))
            
            
            if self.digestion > 20:
                bubble_count = int(self.digestion / 20)
                for i in range(1, bubble_count + 1):
                    angle = self.rotation + i * (2 * math.pi / bubble_count)
                    dist = digestion_radius * 0.7
                    bx = self.x + math.cos(angle) * dist
                    by = self.y + math.sin(angle) * dist
                    bubble_size = max(1, 3 * (self.digestion - 20*i) / 80)
                    pygame.draw.circle(surface, (255, 255, 255, 100), (int(bx), int(by)), int(bubble_size))

class Paramecium:
    def __init__(self):
        self.x = 300
        self.y = HEIGHT // 2
        self.length = 150
        self.width = 60
        self.angle = 0
        self.speed = 1.5
        self.vacuoles = []
        self.cilia_phase = 0
        self.oral_groove_open = True
        self.groove_timer = 0
        self.contractile_vacuole_timer = 0
        self.contractile_vacuole_visible = False
        self.cilia_beating = True
        self.pulse_animation = 0
        self.phagocytosis_active = True  # 
        
    def update(self, yeast_particles):
        
        self.pulse_animation = (self.pulse_animation + 0.05) % (2 * math.pi)
        pulse_offset = math.sin(self.pulse_animation) * 2
        
        
        self.y += math.sin(self.angle) * 2
        self.angle += 0.02
        
        
        if self.y < 100 or self.y > HEIGHT - 100:
            self.angle = -self.angle
            
        
        self.groove_timer += 1
        if self.groove_timer > 60:
            self.oral_groove_open = not self.oral_groove_open
            self.groove_timer = 0
            
        
        self.contractile_vacuole_timer += 1
        if self.contractile_vacuole_timer > 180:  
            self.contractile_vacuole_visible = not self.contractile_vacuole_visible
            self.contractile_vacuole_timer = 0
            
        
        if self.cilia_beating:
            self.cilia_phase = (self.cilia_phase + 0.1) % (2 * math.pi)
        
      
        if self.phagocytosis_active:
            for particle in yeast_particles:
                if not particle.engulfed:
                 
                    groove_x = self.x + self.length//3 + pulse_offset
                    groove_y = self.y
                    groove_width = self.width//2 + pulse_offset
                    
                    distance = math.sqrt((particle.x - groove_x)**2 + (particle.y - groove_y)**2)
                    
                    if distance < groove_width + particle.radius:
                        particle.in_oral_groove = True
                     
                        particle.x += (groove_x - particle.x) * 0.05
                        particle.y += (groove_y - particle.y) * 0.05
                        
                        if distance < particle.radius and self.oral_groove_open:
                            particle.engulfed = True
                            self.vacuoles.append(particle)
                    else:
                        particle.in_oral_groove = False
    
    def draw(self, surface):
        pulse_offset = math.sin(self.pulse_animation) * 2
        
       
        body_length = self.length + pulse_offset
        body_width = self.width + pulse_offset
        pygame.draw.ellipse(surface, PARAMECIUM_COLOR, 
                          (self.x - body_length//2, self.y - body_width//2, 
                           body_length, body_width))
        
      
        groove_width = body_width//2 - 5
        if self.oral_groove_open:
            pygame.draw.ellipse(surface, ORAL_GROOVE_COLOR, 
                              (self.x + body_length//3 - groove_width//2, 
                               self.y - groove_width//2, 
                               groove_width, groove_width))
        else:
            pygame.draw.arc(surface, ORAL_GROOVE_COLOR, 
                          (self.x + body_length//3 - groove_width//2, 
                           self.y - groove_width//2, 
                           groove_width, groove_width), 
                          math.pi/4, 7*math.pi/4, 2)
        
       
        if self.cilia_beating:
            for i in range(20):
                angle = i * (2 * math.pi / 20)
                cilia_x = self.x - body_length//2 * math.cos(angle)
                cilia_y = self.y - body_width//2 * math.sin(angle)
                
                wave = math.sin(self.cilia_phase + i * 0.5) * 8
                pygame.draw.line(surface, CILIA_COLOR, 
                               (cilia_x, cilia_y), 
                               (cilia_x - 15 * math.cos(angle) + wave, 
                                cilia_y - 15 * math.sin(angle) + wave), 2)
        
       
        if self.contractile_vacuole_visible:
            cv_size = 10 + math.sin(self.contractile_vacuole_timer * 0.1) * 5
            pygame.draw.circle(surface, (200, 240, 255), 
                             (int(self.x - body_length//3), int(self.y)), int(cv_size))
            pygame.draw.circle(surface, (100, 150, 200), 
                             (int(self.x - body_length//3), int(self.y)), int(cv_size), 1)
        
       
        for i, vacuole in enumerate(self.vacuoles):
            
            progress = min(1.0, vacuole.digestion / 100)
            vac_x = self.x - body_length//3 + progress * body_length * 0.66
            vac_y = self.y + math.sin(progress * math.pi * 4) * body_width//3
            
            vacuole.x = vac_x
            vacuole.y = vac_y
            vacuole.draw(surface)

class ControlPanel:
    def __init__(self, x, y, width, height):
        self.rect = pygame.Rect(x, y, width, height)
        self.buttons = []
        self.sliders = []
        self.font = pygame.font.SysFont('Arial', 18)
        self.small_font = pygame.font.SysFont('Arial', 14)
        
    def add_button(self, x, y, width, height, text, action):
        btn = Button(self.rect.x + x, self.rect.y + y, width, height, text, action)
        self.buttons.append(btn)
        return btn
        
    def add_slider(self, x, y, width, height, min_val, max_val, initial_val, label):
        slider = Slider(self.rect.x + x, self.rect.y + y, width, height, min_val, max_val, initial_val, label)
        self.sliders.append(slider)
        return slider
        
    def draw(self, surface):
       
        pygame.draw.rect(surface, CONTROL_PANEL_COLOR, self.rect)
        pygame.draw.rect(surface, (0, 0, 0), self.rect, 2)
        
   
        title = self.font.render("Control Panel", True, (0, 0, 0))
        surface.blit(title, (self.rect.x + 10, self.rect.y + 10))
        
       
        for button in self.buttons:
            button.draw(surface)
            
       
        for slider in self.sliders:
            slider.draw(surface)
            
       
        help_text = [
            "Controls:",
            "- SPACE: Add yeast",
            "- P: Pause simulation",
            "- Click & drag sliders",
            "- Buttons toggle features"
        ]
        
        for i, line in enumerate(help_text):
            text_surf = self.small_font.render(line, True, (0, 0, 0))
            surface.blit(text_surf, (self.rect.x + 10, self.rect.y + self.rect.height - 100 + i * 20))
    
    def handle_event(self, event):
        for button in self.buttons:
            if event.type == MOUSEMOTION:
                button.check_hover(event.pos)
            elif event.type == MOUSEBUTTONDOWN:
                button.handle_event(event)
                
        for slider in self.sliders:
            slider.handle_event(event)
    
    def update(self):
        for slider in self.sliders:
            slider.update()

def main():
    
    paramecium = Paramecium()
    
    
    yeast_particles = [YeastParticle() for _ in range(15)]
    
    
    control_panel = ControlPanel(WIDTH - 250, 50, 230, HEIGHT - 100)
    
    
    speed_slider = control_panel.add_slider(10, 50, 200, 20, 0.1, 3.0, 1.0, "Speed")
    particle_slider = control_panel.add_slider(10, 100, 200, 20, 1, 50, 15, "Particles")
    
    
    def toggle_cilia():
        paramecium.cilia_beating = not paramecium.cilia_beating
        cilia_btn.text = f"Cilia: {'ON' if paramecium.cilia_beating else 'OFF'}"
    
    cilia_btn = control_panel.add_button(10, 150, 200, 30, 
                                       f"Cilia: {'ON' if paramecium.cilia_beating else 'OFF'}", 
                                       toggle_cilia)
    
    def toggle_phagocytosis():
        paramecium.phagocytosis_active = not paramecium.phagocytosis_active
        phagocytosis_btn.text = f"Phagocytosis: {'ON' if paramecium.phagocytosis_active else 'OFF'}"
    
    phagocytosis_btn = control_panel.add_button(10, 190, 200, 30, 
                                              f"Phagocytosis: {'ON' if paramecium.phagocytosis_active else 'OFF'}", 
                                              toggle_phagocytosis)
    
    def reset_simulation():
        nonlocal yeast_particles
        yeast_particles = [YeastParticle(speed_slider.value) for _ in range(int(particle_slider.value))]
        paramecium.vacuoles.clear()
    
    control_panel.add_button(10, 230, 200, 30, "Reset Simulation", reset_simulation)
    
    
    simulation_paused = False
    
    
    running = True
    while running:
        
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                elif event.key == K_SPACE:
                    
                    yeast_particles.extend([YeastParticle(speed_slider.value) for _ in range(5)])
                elif event.key == K_p:
                    simulation_paused = not simulation_paused
            
            
            control_panel.handle_event(event)
        
        if not simulation_paused:
            
            control_panel.update()
            
           
            for particle in yeast_particles:
                particle.speed_factor = speed_slider.value
            
            paramecium.update(yeast_particles)
            for particle in yeast_particles:
                particle.update()
            

            yeast_particles = [p for p in yeast_particles if p.digestion < 100 or not p.engulfed]
            
   
            target_count = int(particle_slider.value)
            current_count = len([p for p in yeast_particles if not p.engulfed])
            
            if current_count < target_count and random.random() < 0.02:
                yeast_particles.append(YeastParticle(speed_slider.value))
            elif current_count > target_count and len(yeast_particles) > 0:

                for i, p in enumerate(yeast_particles):
                    if not p.engulfed:
                        yeast_particles.pop(i)
                        break
        

        screen.fill(BACKGROUND)
        

        for particle in yeast_particles:
            if not particle.engulfed:
                particle.draw(screen)
        

        paramecium.draw(screen)
        

        control_panel.draw(screen)
        

        font = pygame.font.SysFont('Arial', 16)
        stats = f"Yeast: {len([p for p in yeast_particles if not p.engulfed])} | " \
                f"Vacuoles: {len(paramecium.vacuoles)} | " \
                f"Status: {'Paused' if simulation_paused else 'Running'}"
        text = font.render(stats, True, (0, 0, 0))
        screen.blit(text, (10, 10))
        
        pygame.display.flip()
        clock.tick(FPS)
    
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
