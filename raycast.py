import pygame
import math

worldMap = [
            [1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 3, 0, 0, 2],
            [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 3, 1, 0, 0, 2, 0, 0, 0, 2, 3, 2, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 1, 2, 0, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 2, 0, 0, 2, 1, 0, 0, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 3, 1, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
            [1, 0, 2, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2],
            [2, 0, 3, 0, 0, 2, 0, 0, 0, 0, 0, 0, 0, 2, 3, 2, 1, 2, 0, 1],
            [1, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
            [2, 3, 1, 0, 0, 2, 0, 0, 2, 1, 3, 2, 0, 2, 0, 0, 3, 0, 3, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1, 0, 0, 2, 0, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 2, 3, 0, 1, 2, 0, 1],
            [1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 0, 0, 3, 0, 2],
            [2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 3, 0, 0, 0, 1],
            [2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1, 2, 1]]

keys = [False] * 324


def exit():
    pygame.display.quit()
    pygame.quit()


def main():
    pygame.init()

    font = pygame.font.SysFont("Arial", 18)
    hud = font.render("Test", True, (0, 0, 0))

    width = 1080
    height = 720


    screen = pygame.display.set_mode((width, height))

    position_x = 3.0
    position_y = 7.0

    direction_x = 1.0
    direction_y = 0

    plane_x = 0
    plane_y = .5

    rotation_speed = .008
    move_speed = .03

    trig = (math.cos(rotation_speed), math.sin(rotation_speed))
    inverse_trig = (math.cos(-rotation_speed), math.sin(-rotation_speed))
    cos, sin = (0, 1)

    done = False

    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True

            if event.type == pygame.KEYDOWN:
                keys[event.key] = True

            elif event.type == pygame.KEYUP:
                keys[event.key] = False

        if keys[pygame.K_ESCAPE]:
            done = True

        if keys[pygame.K_LEFT]:
            old_direction_x = direction_x
            direction_x = direction_x * inverse_trig[cos] - direction_y * inverse_trig[sin]
            direction_y = old_direction_x * inverse_trig[sin] + direction_y * inverse_trig[cos]

            old_plane_x = plane_x
            plane_x = plane_x * inverse_trig[cos] - plane_y * inverse_trig[sin]
            plane_y = old_plane_x * inverse_trig[sin] + plane_y * inverse_trig[cos]

        if keys[pygame.K_RIGHT]:
            old_direction_x = direction_x
            direction_x = direction_x * trig[cos] - direction_y * trig[sin]
            direction_y = old_direction_x * trig[sin] + direction_y * trig[cos]

            old_plane_x = plane_x
            plane_x = plane_x * trig[cos] - plane_y * trig[sin]
            plane_y = old_plane_x * trig[sin] + plane_y * trig[cos]

        if keys[pygame.K_UP]:
            if not worldMap[int(position_x + direction_x * move_speed)][int(position_y)]:
                position_x += direction_x * move_speed
            if not worldMap[int(position_x)][int(position_y + direction_y * move_speed)]:
                position_y += direction_y * move_speed

        if keys[pygame.K_DOWN]:
            if not worldMap[int(position_x - direction_x * move_speed)][int(position_y)]:
                position_x -= direction_x * move_speed
            if not worldMap[int(position_x)][int(position_y - direction_y * move_speed)]:
                position_y -= direction_y * move_speed

        screen.fill((25, 25, 25))
        pygame.draw.rect(screen, (50, 50, 50), (0, height/2, width, height/2))

        column = 0
        while column < width:
            camera_x = 2 * column / width - 1.0

            ray_position_x = position_x
            ray_position_y = position_y

            ray_direction_x = direction_x + plane_x * camera_x
            ray_direction_y = direction_y + plane_y * camera_x + .000000000000001

            map_x = int(ray_position_x)
            map_y = int(ray_position_y)

            delta_distance_x = math.sqrt(1.0 + (ray_direction_y * ray_direction_y) / (ray_direction_x * ray_direction_x))
            delta_distance_y = math.sqrt(1.0 + (ray_direction_x * ray_direction_x) / (ray_direction_y * ray_direction_y))

            if ray_direction_x < 0:
                step_x = -1
                side_distance_x = (ray_position_x - map_x) * delta_distance_x

            else:
                step_x = 1
                side_distance_x = (map_x + 1.0 - ray_position_x) * delta_distance_x

            if ray_direction_y < 0:
                step_y = -1
                side_distance_y = (ray_position_y - map_y) * delta_distance_y
            else:
                step_y = 1
                side_distance_y = (map_y + 1.0 - ray_position_y) * delta_distance_y

            hit = 0
            side = 0
            while hit == 0:
                if side_distance_x < side_distance_y:
                    side_distance_x += delta_distance_x
                    map_x += step_x
                    side = 0

                else:
                    side_distance_y += delta_distance_y
                    map_y += step_y
                    side = 1

                if worldMap[map_x][map_y] > 0:
                    hit = 1

            if side == 0:
                perp_wall_distance = abs((map_x - ray_position_x + (1.0 - step_x) / 2.0) / ray_direction_x)
            else:
                perp_wall_distance = abs((map_y - ray_position_y + ( 1.0 - step_y ) / 2.0) / ray_direction_y)

            line_height = abs(int(height / perp_wall_distance + .0000001))
            draw_start = -line_height / 2.0 + height / 2.0

            if draw_start < 0:
                draw_start = 0

            draw_end = line_height / 2.0 + height / 2.0

            if draw_end >= height:
                draw_end = height - 1

            wall_colors = [[], [150, 0, 0], [0, 150, 0], [0, 0, 150]]
            color = wall_colors[worldMap[map_x][map_y]]

            if side == 1:
                for i, v in enumerate(color):
                    color[i] = int(v >> 1)

            pygame.draw.line(screen, color, (column, draw_start), (column, draw_end), 3)
            column += 3

        pygame.event.pump()
        pygame.display.update()

    exit()




if __name__ == '__main__':
    main()
