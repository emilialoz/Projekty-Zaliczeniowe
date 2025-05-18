if (!require(MASS)) install.packages("MASS", dependencies = TRUE)
library(MASS)
data("Cars93")
## Oblicz średnią wagę samochodów
avg_weight <- mean(Cars93$Weight, na.rm = TRUE)
cat("Średnia waga samochodów wynosi:", avg_weight, "\n")


## Znajdź najdroższy samochód
expensive_poz <- which.max(Cars93$Price)
most_expensive_name<- as.character(Cars93$Make[expensive_poz])
cat("Najdroższy samochód to ", most_expensive_name)


## Oblicz średnią liczbę cylindrów
Cars93$Cylinders <- as.numeric(Cars93$Cylinders)
mean_cylinders <- mean(Cars93$Cylinders, na.rm = TRUE)
cat("Średnia liczba cylindrów wynosi:", mean_cylinders, "\n")


## Vany spoza USA
foreign_vans <- subset(Cars93, Type == "Van" & Origin != "USA")
cat("Vany spoza USA:\n")
print(foreign_vans)


## Samochody, których model zawiera cyfry
cars_with_digits <- Cars93[grepl("[0-9]", Cars93$Model), ]
cat("Samochody, których model zawiera cyfry:\n")
print(cars_with_digits)



## Samochody z USA, szersze niż jakikolwiek model Toyoty lub Subaru
max_width_toyota_subaru <- max(Cars93$Width[Cars93$Make %in% c("Toyota", "Subaru")], na.rm = TRUE)
wide_usa_cars <- subset(Cars93, Origin == "USA" & Width > max_width_toyota_subaru)
cat("Auta z USA szersze niż Toyota/Subaru:\n")
print(wide_usa_cars)