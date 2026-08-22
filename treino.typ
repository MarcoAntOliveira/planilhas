#let results = csv("treino2.csv")
#set text(size: 12pt)
#table(
  columns: (1fr,1fr,1fr,1fr,1fr,1fr,1fr,1fr),
  ..results.flatten(),
)