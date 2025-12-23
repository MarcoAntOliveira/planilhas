#let results = csv("treino.csv")

#table(
  columns: 8,
  ..results.flatten(),
)
