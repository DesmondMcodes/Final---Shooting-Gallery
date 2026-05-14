# Final---Shooting-Gallery
Shooting Gallery is a two-player arcade-style game where players compete to shoot falling blocks and earn points. Rows of blocks continuously descend from the top of the screen, and players must aim and fire bullets to destroy them before they reach the bottom.

Some blocks require multiple hits to destroy, while special bomb blocks explode and clear nearby blocks when struck. 




## Player Class
- Will remain near the bottom of the screen and rotate to aim shots.
- Movement is controlled by key presses:
    - Turn left
    - Turn right
    - Fire bullets
- The player’s heading determines the direction of fired bullets.
- Each player can have a maximum of 5 bullets on screen at a time.
- Each player has a score that increases when blocks are destroyed.
## Block Class
- Blocks are arranged in rows and continuously move downward over time.
- Each block has 3 health states:
    - First hit → changes color (e.g., gray → orange)
    - Second hit → changes color again (e.g., orange → red)
    - Third hit → block is destroyed
- When destroyed:
    - The block is removed from the game
    - The player earns +1 point
    #### Bomb Blocks 
    - Bomb blocks are a different color (e.g., green).
    - When hit:
        - They detonate immediately
        - All blocks within a certain radius are removed
    - Bomb blocks do not require multiple hits to activate.
## Bullet Class
- Bullets are created when a player presses the fire key.
- Each bullet:
    - Starts at the player’s position
    - Travels in the direction of the player’s heading
    - Move continuously forward
    - Bounce off the left and right walls
    - Are removed if they leave the top of the screen
- If a bullet hits a block:
    - The bullet is destroyed
    - The block’s strike() method is triggered
## Score Class
- Displays each player’s score on the screen.
- Updates whenever a player destroys a block.
- Each player has their own score display.
## Game Mechanics
- Blocks are generated in rows at the top of the screen.
- Every 2 seconds:
    - All blocks move downward
    - A new row of blocks is added
- The game continues as long as players can keep blocks from reaching the bottom or touching a player.
## Collision Rules
- If a bullet collides with a block:
    - The bullet is removed
    - The block is damaged or destroyed
- If a bomb block is hit:
    - All nearby blocks are removed
    