library(VGAM)
options(scipen= 999 )
x_ = function(z, n){
  return (mean(z))
}
medX = function(z, n){
  #return (median(z))
  l=n%/%2
  if(n%%2==1){
    return (z[l+1])
  }
  else{
    return ((z[l]+z[l+1])/2)
  }
}
z_R = function(z, n){
  return((z[1]+z[n])/2)  
}
z_p = function(z, n, p){
  if((n*p)%%1==0){
    return(z[n*p])
  }
  else{
    return(z[(n*p)%/%1+1])
  }
}

z_Q = function(z,n){
  return ((z_p(z,n,1/4)+z_p(z,n,3/4))/2)
}
z_tr = function(z,n){
  r=n%/%4
  r=n%/%4
  tmp=0
  for (i in (1+r):(n-r)){
    tmp = tmp + z[i]
  }
  return(tmp/(n-2*r))
}
E_z = function(z,n){
  return(x_(z,n))
}
D_z = function(z,n){
  tmp=0
  tmp2=x_(z,n)
  tmp3=mean(z)
  for (i in 1:n){
    #cat("z[i]=", z[i], "x_=", tmp2, "\n")
    tmp = tmp + ((z[i])-tmp2)*((z[i])-tmp2)
  }
  return(tmp/n)
}

lab2 = function(N, n){
  
  tmp_x_ <- rep(0,N)
  tmp_medX <- rep(0,N)
  tmp_z_R <- rep(0,N)
  tmp_z_Q <- rep(0,N)
  tmp_z_tr <- rep(0,N)
  
  for (i in 1:N){
    #x <- rnorm(n, mean = 0, sd = 1)
    #x <- rcauchy(n, location = 0, scale = 1)
    #x <- rlaplace(n, loc=0, scale=1/sqrt(2))
    #x <- rpois(n, lambda = 10)
    x <- runif(n, min = -3, max = 3)
    x <- sort(x)
    tmp_x_[i]=x_(x,n)
    tmp_medX[i]=medX(x,n)
    tmp_z_R[i]=z_R(x,n)
    tmp_z_Q[i]=z_Q(x,n)
    tmp_z_tr[i]=z_tr(x,n)
  }
  cat("x_   med   z_r   z_Q   z_tr")
  
  
  cat("\n$E(z)$  &", round(E_z(tmp_x_,N),digits = 4), "&", round(E_z(tmp_medX,N),digits = 4), "&", round(E_z(tmp_z_R,N),digits = 4), "&", round(E_z(tmp_z_Q,N),digits = 4), "&", round(E_z(tmp_z_tr,N),digits = 4), " \\\ hline" )
  cat("\n$E(z)$  &", round(D_z(tmp_x_,N),digits = 4), "&", round(D_z(tmp_medX,N),digits = 4), "&", round(D_z(tmp_z_R,N),digits = 4), "&", round(D_z(tmp_z_Q,N),digits = 4), "&", round(D_z(tmp_z_tr,N),digits = 4), " \\\ hline" )
  
  T1<-c(round(round(E_z(tmp_x_,N),digits = 4)-sqrt(round(D_z(tmp_x_,N),digits = 4)),digits = 4),round(round(E_z(tmp_x_,N),digits = 4)+sqrt(round(D_z(tmp_x_,N),digits = 4)),digits = 4))
  T2<-c(round(round(E_z(tmp_medX,N),digits = 4)-sqrt(round(D_z(tmp_medX,N),digits = 4)),digits = 4),round(round(E_z(tmp_medX,N),digits = 4)+sqrt(round(D_z(tmp_medX,N),digits = 4)),digits = 4))
  T3<-c(round(round(E_z(tmp_z_R,N),digits = 4)-sqrt(round(D_z(tmp_z_R,N),digits = 4)),digits = 4),round(round(E_z(tmp_z_R,N),digits = 4)+sqrt(round(D_z(tmp_z_R,N),digits = 4)),digits = 4))
  T4<-c(round(round(E_z(tmp_z_Q,N),digits = 4)-sqrt(round(D_z(tmp_z_Q,N),digits = 4)),digits = 4),round(round(E_z(tmp_z_Q,N),digits = 4)+sqrt(round(D_z(tmp_z_Q,N),digits = 4)),digits = 4))
  T5<-c(round(round(E_z(tmp_z_tr,N),digits = 4)-sqrt(round(D_z(tmp_z_tr,N),digits = 4)),digits = 4),round(round(E_z(tmp_z_tr,N),digits = 4)+sqrt(round(D_z(tmp_z_tr,N),digits = 4)),digits = 4))
  
  cat("\n$E(z) \ pm \ sqrt{D(z)}$  & [", T1[1],";", T1[2], "]", "&", "[", T2[1],";", T2[2], "]","&", "[", T3[1],";", T3[2], "]","&", "[", T4[1],";", T4[2], "]", "&", "[", T5[1],";", T5[2], "]", " \\\ hline" )
 
}

lab2(1000, 1000)