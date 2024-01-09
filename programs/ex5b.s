    Z <- Z + 1
[A] IF X1 != 0 GOTO B
    IF Z != 0 GOTO E
[B] X1 <- X1 - 1
[C] IF X2 != 0 GOTO D
    IF Z !=  0 GOTO F
[D] X2 <- X2 - 1
    Z2 <- Z2 + 1
    Y <- Y + 1
    IF Z != 0 GOTO C
[F] IF Z2 != 0 GOTO G
    IF Z != 0 GOTO A
[G] Z2 <- Z2 - 1
    X2 <- X2 + 1
    IF Z != 0 GOTO F