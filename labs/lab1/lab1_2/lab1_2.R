library(VGAM)
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
  cat("\nE(z)  ", E_z(tmp_x_,N), "&", E_z(tmp_medX,N), "&", E_z(tmp_z_R,N), "&", E_z(tmp_z_Q,N), "&", E_z(tmp_z_tr,N), " " )
  cat("\nD(z)  ", D_z(tmp_x_,N), "&", D_z(tmp_medX,N), "&", D_z(tmp_z_R,N), "&", D_z(tmp_z_Q,N), "&", D_z(tmp_z_tr,N), " " )
}

lab2(1000, 1000)