program recursion
    implicit none

    contains

    recursive function horner(arr,x) result (res)
        implicit none

        real(kind=8),   intent(in) :: arr(:), x
        real(kind=8) :: res

        if (size(arr) == 1) then
            res = arr(1)
        else
            res = arr(1) + x * horner(arr(2:),x)
        endif

    end function horner

    recursive subroutine fibonacci(arr,n)
        implicit none
        integer, intent(in) :: n
        integer, intent(out) :: arr(:)

        if (n == 2) then
            arr = [0, 1]
        else
            call fibonacci(arr(1:n-1),n-1)
            arr(n) = arr(n-1) + arr(n-2)
        end if
    end subroutine fibonacci


    recursive function factorial(n) result(res)
        implicit none 

        integer,    intent(in) :: n
        integer :: res

        if (n <= 1) then
            res = 1
        else
            res = n * factorial(n-1)
        endif

    end function factorial

    recursive function binomial(n,k) result(res)
        implicit none

        integer,    intent(in) :: n, k
        integer :: res

        if (n >= 0 .and. k == 0) then 
            res = 1
        elseif (n == 0 .and. k > 0) then 
            res = 0
        else
            res = binomial(n-1,k-1) + binomial(n-1,k)
        endif

    end function binomial
    
end program recursion