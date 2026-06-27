program recursion
    implicit none

    integer, allocatable :: fib_array(:)
    integer :: m

    m = 10
    allocate(fib_array(m))

    call fibonacci(m,fib_array)

    print*, fib_array

    contains

    recursive subroutine fibonacci(n, arr)
        implicit none
        integer, intent(in) :: n
        integer, intent(out) :: arr(n)

        if (n == 1) then
            arr(1) = 0
        elseif (n == 2) then
            arr = [0, 1]
        else
            call fibonacci(n-1, arr(1:n-1))
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