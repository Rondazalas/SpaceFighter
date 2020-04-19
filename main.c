#define xRes 100
#define yRes 200
#define modRes 5
#define spritesFile "spriteTable"

typedef unsigned char s_byte // data of 1 byte (8 bits) in size
typedef unsigned short s_2byte // data of 2 byte (16 bits) in size

struct sprite
{
	s_byte *name;
	s_byte nameLength;
	s_byte width;
	s_byte height;
	s_byte *sprite;
	struct sprite *next;
}

struct engine
{
	s_byte xSpeed; // speed of x velocity for ship
	//s_byte ySpeed; // how fast the ship 
	//s_byte boostSpeed; // The modifier for new speed when boosting
	//s_byte boostHang; // How long the ship stays at Boost speed
	//s_byte boostLength; // How long it takes to decelerate from Boost speed to Normal speed
	//s_byte boostCooldown; // How long until player can boost again
}

struct projectile
{
	s_byte (*properties)(struct projectile); // modifies properties of structure 
	s_byte xPos; // x-axis position
	s_byte yPos; // y-axis position
	s_byte xVel; // how fast the projectile will move horizontally
	s_byte yVel; // how fast the projectile will move vertically
	s_byte hitbox; // size of hitbox for projectile
}

struct weapon
{
	struct projectile projectile;
	s_byte fireRate; // number of frames weapon must wait until it fires again
	s_byte fireCooldown; // remaining frames until weapon can fire again
}

struct playerShip
{
	s_byte facing; // direction that the ship/weapon should fire in
	struct engine engine;
	struct weapon weapon;
	s_byte hurtbox; // size of the hurtbox for this ship
	struct sprite sprite;
}

struct projectile propStandard(struct projectile projectile)
{
	projectile.xPos -= xVel;
	projectile.yPos -= yVel;
	return projectile;
}

struct weapon wepStandard(s_byte xPos, s_byte yPos)
{
	struct weapon weapon;
	weapon.fireRate = 60;
	weapon.fireCooldown = 0;

	weapon.projectile.properties = &propStandard;
	weapon.projectile.xPos = xPos;
	weapon.projectile.yPos = yPos;
	weapon.projectile.xVel = 0;
	weapon.projectile.yVel = 10;
	weapon.projectile.hitbox = 10;

	return projectile;
}

struct engine engStandard()
{
	struct engine engine;
	engine.xSpeed = 1;
	return engine
}

struct playerShip initializePlayerShip()
{
	struct playerShip playerShip;
	playerShip.weapon = wepStandard;
	playerShip.engine = engStandard();
}



int main()
{
	// initialize ships
	struct playerShip playerShip = initializePlayerShip();

	s_byte gfx[xRes][yRes];
	s_byte hitboxes[xRes][yRes];
}