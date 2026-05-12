def analyze_board_game(board_size: int) -> dict:
  # Analisa o jogo de tabuleiro simples com movimentos de 1, 2 ou 3 casas
  if not isinstance(board_size, int):
    raise TypeError("The board size must be an integer.")

  if board_size < 3:
    raise ValueError("The board must have at least 3 spaces.")

  minimum_turns = (board_size + 2) // 3

  optimal_combinations = count_combinations_with_exact_length(
    total=board_size,
    length=minimum_turns
  )

  # Probabilidade de atingir o final com o número mínimo de jogadas
  optimal_path_probability = optimal_combinations / (3 ** minimum_turns)

  combinations_without_looping = count_combinations_without_looping(board_size)

  return {
    "minimum_turns": minimum_turns,
    "optimal_path_probability": optimal_path_probability,
    "combinations_without_looping": combinations_without_looping
  }


def count_combinations_with_exact_length(total: int, length: int) -> int:
  # Conta sequências de movimentos que somam exatamente ao total
  dp = [[0] * (total + 1) for _ in range(length + 1)]
  dp[0][0] = 1

  for current_length in range(1, length + 1):
    for current_sum in range(total + 1):
      for move in (1, 2, 3):
        previous_sum = current_sum - move

        if previous_sum >= 0:
          dp[current_length][current_sum] += dp[current_length - 1][previous_sum]

  return dp[length][total]


def count_combinations_without_looping(total: int) -> int:
  # Conta todas as maneiras possíveis de chegar ao total sem restrição de número de movimentos
  dp = [0] * (total + 1)
  dp[0] = 1

  for current_sum in range(1, total + 1):
    for move in (1, 2, 3):
      previous_sum = current_sum - move

      if previous_sum >= 0:
        dp[current_sum] += dp[previous_sum]

  return dp[total]


print(analyze_board_game(5))