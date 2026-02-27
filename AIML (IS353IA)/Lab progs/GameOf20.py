def minimax(total, is_ai_turn, alpha, beta):
    # Base case: If total is 20 or more, the game is over
    if total >= 20:
        return -1 if is_ai_turn else 1  # -1 if AI loses, 1 if AI wins
    
    # Set initial evaluation depending on whose turn it is
    best_eval = -float('inf') if is_ai_turn else float('inf')
    
    # Explore each possible move (1, 2, or 3)
    for i in range(1, 4):
        eval = minimax(total + i, not is_ai_turn, alpha, beta)  # Recursive call for the next move
        
        # Maximize if it's AI's turn, else minimize
        if is_ai_turn:
            best_eval = max(best_eval, eval)
            alpha = max(alpha, eval)
        else:
            best_eval = min(best_eval, eval)
            beta = min(beta, eval)
        
        # Alpha-beta pruning to cut off unnecessary branches
        if beta <= alpha:
            break
    return best_eval

total = 0  # Initialize total score

# Game loop
while total < 20:
    # Human player's move
    human_move = int(input("Enter your move (1, 2, or 3): "))
    while human_move not in [1, 2, 3]:  # Validate input
        human_move = int(input("Invalid move. Enter 1, 2, or 3: "))
    total += human_move
    print(f"Total after your move: {total}")
    
    # Check if human wins
    if total >= 20:
        print("You win!")
        break

    # AI's turn
    print("AI is making its move...")
    # Select the best move by calling minimax on each possible option
    best_move = max((minimax(total + i, False, -float('inf'), float('inf')), i) for i in range(1, 4))[1]
    total += best_move
    print(f"AI adds {best_move}. Total is {total}")
    
    # Check if AI wins
    if total >= 20:
        print("AI wins!")
        break