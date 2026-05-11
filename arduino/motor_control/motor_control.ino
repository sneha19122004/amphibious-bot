/*
 * Amphibious Robot - Motor Control via Bluetooth (HC-05)
 * 
 * Hardware:
 *   - Arduino Uno
 *   - HC-05 Bluetooth Module
 *   - L293N / L298N Motor Driver
 *   - 2x DC Motors (Left & Right screw wheels)
 *
 * Commands (sent from Bluetooth RC Controller app):
 *   F = Forward
 *   B = Backward
 *   L = Turn Left
 *   R = Turn Right
 *   S = Stop
 *
 * Team: Akshay Raj B, Nandana Sunil, Sneha Alphonso Francis, Swaroop S
 * Guide: Mr. Sreedeep Krishnan
 * Adi Shankara Institute of Engineering and Technology, Kalady
 */

// ── Motor A (LEFT MOTOR) pin definitions ──
const int motorA1 = 3;
const int motorA2 = 4;
const int enableA = 5;

// ── Motor B (RIGHT MOTOR) pin definitions ──
const int motorB1 = 6;
const int motorB2 = 7;
const int enableB = 9;

// ── Function prototypes ──
void moveForward();
void moveBackward();
void turnLeft();
void turnRight();
void stopCar();

void setup() {
  // Set motor pins as outputs
  pinMode(motorA1, OUTPUT);
  pinMode(motorA2, OUTPUT);
  pinMode(enableA, OUTPUT);

  pinMode(motorB1, OUTPUT);
  pinMode(motorB2, OUTPUT);
  pinMode(enableB, OUTPUT);

  // Initialize Bluetooth serial communication
  Serial.begin(9600);

  // Enable both motors
  digitalWrite(enableA, HIGH);
  digitalWrite(enableB, HIGH);
}

void loop() {
  // Check if data is available from HC-05 Bluetooth module
  if (Serial.available() > 0) {
    char command = Serial.read(); // Read the command sent from the phone

    // Control the robot based on the Bluetooth command
    switch (command) {
      case 'F':  // Forward
        moveForward();
        break;
      case 'B':  // Backward
        moveBackward();
        break;
      case 'L':  // Left
        turnLeft();
        break;
      case 'R':  // Right
        turnRight();
        break;
      case 'S':  // Stop
        stopCar();
        break;
      default:
        stopCar();
        break;
    }
  }
}

// ─────────────────────────────────────────────
// Motor control functions
// Motor A = LEFT MOTOR | Motor B = RIGHT MOTOR
// ─────────────────────────────────────────────

void moveForward() {
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, HIGH);
}

void moveBackward() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, HIGH);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
}

void turnLeft() {
  // Motor A stops, Motor B drives forward
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, HIGH);
  digitalWrite(motorB2, LOW);
}

void turnRight() {
  // Motor A drives forward, Motor B stops
  digitalWrite(motorA1, HIGH);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
}

void stopCar() {
  digitalWrite(motorA1, LOW);
  digitalWrite(motorA2, LOW);
  digitalWrite(motorB1, LOW);
  digitalWrite(motorB2, LOW);
}
