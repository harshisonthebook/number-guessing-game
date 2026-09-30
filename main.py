import random


rounds_played = 0
winning_attempts = []

while True:
	rounds_played += 1
	difficulty = input("Choose difficulty (easy/medium/hard): ").strip().lower()
	lower_bound, upper_bound, attempt_limit = 1, 100, 7

	if difficulty == "easy":
		lower_bound, upper_bound, attempt_limit = 1, 50, 10

	if difficulty == "hard":
		print("Hard mode is not ready yet. Using medium difficulty.")
	elif difficulty not in ("easy", "medium"):
		print("Unknown difficulty. Using medium difficulty.")

	number = random.randint(lower_bound, upper_bound)
	print(f"I'm thinking of a number from {lower_bound} to {upper_bound}.")

	for attempt in range(1, attempt_limit + 1):
		while True:
			try:
				guess = int(input(f"Attempt {attempt}/{attempt_limit}. Your guess: "))
			except ValueError:
				print("Enter a whole number.")
				continue

			if not lower_bound <= guess <= upper_bound:
				print(f"Enter a number from {lower_bound} to {upper_bound}.")
				continue
			break

		if guess == number:
			print("Correct! You guessed it.")
			winning_attempts.append(attempt)
			break

		if guess > number:
			feedback = "Too high."
		else:
			feedback = "Too low."

		if abs(guess - number) <= 5:
			feedback = f"Very close! {feedback}"
		print(feedback)
	else:
		print(f"No attempts left. The number was {number}.")

	if input("Play again? (y/n) ").strip().lower() != "y":
		break

total_attempts = 0
best_round = None

for round_number, attempts_used in enumerate(winning_attempts, start=1):
	print(f"Winning round {round_number}: {attempts_used} attempt(s)")
	total_attempts += attempts_used
	if best_round is None or attempts_used < best_round:
		best_round = attempts_used

print(f"Rounds played: {rounds_played}")
print(f"Wins: {len(winning_attempts)}")
if winning_attempts:
	average_attempts = total_attempts / len(winning_attempts)
	print(f"Best round: {best_round} attempt(s)")
	print(f"Average attempts: {average_attempts:.2f}")
else:
	print("Best round: N/A")
	print("Average attempts: N/A")
