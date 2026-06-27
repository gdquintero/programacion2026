program merge
    implicit none
    
    real(kind=8), allocatable :: arr(:)
    real(kind=8) :: star, finish
    integer :: k, n

    n = 10000
    arr = [(real(k, kind=8), k = n, 1, -1)]

    ! call cpu_time(star)
    ! call bubble_sort(arr)
    ! call cpu_time(finish)

    

    contains

    subroutine merge_sort(v)
        implicit none

        real(kind=8),   intent(inout) :: v(:)

    end subroutine merge_sort
end program merge