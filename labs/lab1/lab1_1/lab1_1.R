library(VGAM)

lab1_plot = function(f_n, x_rdist, x_for_ddist, f_ddist, f_filename, f_breaks, f_label){
  # output to be present as PNG file
  png(file = f_filename)
  
  # Create the histogram
  hist(x_rdist, 
       prob = TRUE,
       breaks = f_breaks,
       main = f_label,
       xlab = paste("n =",f_n),
       ylab = "distribution",
  )
  lines(x_for_ddist, f_ddist, col = "red", lwd = 2)
  
  # Save the file.
  dev.off()
}

lab1_norm = function(n, n_breaks, location){
  x_rnorm <- rnorm(n)
  x_for_dnorm <- seq(min(x_rnorm), max(x_rnorm), length = n)
  f_dnorm <- dnorm(x_for_dnorm, mean = mean(x_rnorm), sd = sd(x_rnorm))
  filename_norm = paste(location, "n =", n, "normal distribution.png")
  
  lab1_plot(n, x_rnorm, x_for_dnorm, f_dnorm, filename_norm, n_breaks, "Normal distribution")
}

lab1_unif = function(n, n_breaks, location){
  x_runif <- runif(n, min = -sqrt(3), max = sqrt(3))
  x_for_dunif <- seq(min(x_runif),max(x_runif),length=n)
  f_dunif <- dunif(x_for_dunif, min = -sqrt(3), max = sqrt(3))
  filename_unif = paste(location, "n =", n, "uniform distribution.png")
  
  lab1_plot(n, x_runif, x_for_dunif, f_dunif, filename_unif, n_breaks, "Uniform distribution")
}

lab1_cauchy = function(n, n_breaks, location){
  x_rcauchy <- rcauchy(n, location = 0, scale = 1)
  x_for_dcauchy <- seq(min(x_rcauchy),max(x_rcauchy),length=n)
  f_dcauchy <- dcauchy(x_for_dcauchy, location = 0, scale = 1, log = FALSE)
  filename_cauchy = paste(location, "n =", n, "cauchy distribution.png")
  
  lab1_plot(n, x_rcauchy, x_for_dcauchy, f_dcauchy, filename_cauchy, n_breaks, "Cauchy distribution")
}

lab1_pois = function(n, n_breaks, location){
  x_rpois <- rpois(n, lambda = 10)
  x_for_dpois <- seq(0, max(x_rpois), by = 1)
  f_dpois <- dpois(x_for_dpois, lambda = 10)
  filename_pois = paste(location, "n =", n, "poisson distribution.png")
  
  lab1_plot(n, x_rpois, x_for_dpois, f_dpois, filename_pois, n_breaks, "Poisson distribution")
}

lab1_lap = function(n, n_breaks, location){
  x_rlap <- rlaplace(n, loc=0, scale=1/sqrt(2))
  x_for_dlap <- seq(min(x_rlap),max(x_rlap),length=n)
  f_dlap <- dlaplace(x_for_dlap, location = 0, scale= 1/sqrt(2))
  filename_lap = paste(location, "n =", n, "laplace distribution.png")
  
  lab1_plot(n, x_rlap, x_for_dlap, f_dlap, filename_lap, n_breaks, "Laplace distribution")
}
lab1_1 = function(){
  sizes<-c(10, 100, 1000)
  location="E:/_study/3 course/6th semester/MathStat/labs/lab1/lab1_1/pictures/"
  for (i in sizes){
    if(i==10){
      lab1_norm(i, 5, location)
      lab1_cauchy(i, 5, location)
      lab1_lap(i, 5, location)
      lab1_pois(i, 5, location)
      lab1_unif(i, 5, location)
    }
    else{
      lab1_norm(i, 15, location)
      lab1_cauchy(i, 15, location)
      lab1_lap(i, 15, location)
      lab1_pois(i, 15, location)
      lab1_unif(i, 15, location)
    }
  }
}

lab1_1()