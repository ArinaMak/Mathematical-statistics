library(VGAM)
q13 = function(N, n){
  q_1=0
  q_3=0
  x_1=0
  x_2=0
  for (i in 1:N){
    
    #data <- rnorm(n, mean = 0, sd = 1)
    #data <- rcauchy(n, location = 0, scale = 1)
    #data <- rlaplace(n, loc=0, scale=1/sqrt(2))
    #data <- rpois(n, lambda = 10)
    data <- runif(n, min = -sqrt(3), max = sqrt(3))
    
    q_1=q_1 + quantile(data, 0.25)
    q_3=q_3 + quantile(data, 0.75)
    
    x_1=x_1+quantile(data, 0.25) - 3 / 2 * (quantile(data, 0.75) - quantile(data, 0.25))
    x_2=x_2+quantile(data, 0.75) + 3 / 2 * (quantile(data, 0.75) - quantile(data, 0.25))
  }
  
  cat("\nQ1 & Q3  ", q_1/N, "&", q_3/N)
  cat("\nx1 & x2  ", x_1/N, "&", x_2/N)
}

count_out = function(data){
  q_1<-quantile(data, 0.25)
  q_3<-quantile(data, 0.75)
  
  x_1<-q_1 - 3 / 2 * (q_3 - q_1)
  x_2<-q_3 + 3 / 2 * (q_3 - q_1)
  len=0
  
  for (i in 1:length(data)){
    if(data[i]<x_1 || data[i]>x_2){
      len=len+1
    }
  } 
  return(len)
}

lab3_share_of_emissions=function(N){
  n1=20
  n2=100
  len1=0
  len2=0
  sum=0
  for (i in 1:N){
    data1 <- rnorm(n1, mean = 0, sd = 1)
    data2 <- rnorm(n2, mean = 0, sd = 1)
    #data1 <- rcauchy(n1, location = 0, scale = 1)
    #data2 <- rcauchy(n2, location = 0, scale = 1)
    #data1 <- rlaplace(n1, loc=0, scale=1/sqrt(2))
    #data2 <- rlaplace(n2, loc=0, scale=1/sqrt(2))
    #data1 <- rpois(n1, lambda = 10)
    #data2 <- rpois(n2, lambda = 10)
    #data1 <- runif(n1, min = -3, max = 3)
    #data2 <- runif(n2, min = -3, max = 3)
    
    len1=len1+count_out(data1)
    len2=len2+count_out(data2)
  }
  
  cat("\nshare_of_emissions   ", len1/(N*n1), "&", len2/(N*n2), "\n")
  return(list(len1/(N*n1), len2/(N*n2)))
}

draw_boxplot = function(){
  n1=20
  n2=100
  
  boxplotname="normal distribution"
  data1 <- rnorm(n1, mean = 0, sd = 1)
  data2 <- rnorm(n2, mean = 0, sd = 1)
  #boxplotname="cauchy distribution"
  #data1 <- rcauchy(n1, location = 0, scale = 1)
  #data2 <- rcauchy(n2, location = 0, scale = 1)
  #boxplotname="laplace distribution"
  #data1 <- rlaplace(n1, loc=0, scale=1/sqrt(2))
  #data2 <- rlaplace(n2, loc=0, scale=1/sqrt(2))
  #boxplotname="poisson distribution"
  #data1 <- rpois(n1, lambda = 10)
  #data2 <- rpois(n2, lambda = 10)
  #boxplotname="uniform distribution"
  #data1 <- runif(n1, min = -3, max = 3)
  #data2 <- runif(n2, min = -3, max = 3)
  
  data <- data.frame( "n 20" = data1,
                      "n 100" = data2
  )
  res <- boxplot(data, horizontal = TRUE, main=boxplotname)
  
}

lab3_share_of_emissions(1000)
q13(1000, 100)
draw_boxplot()