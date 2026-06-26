program bubble
    implicit none

    real(kind=8), allocatable :: arr(:)
    real(kind=8) :: star, finish
    integer :: k, n

    n = 10000
    arr = [(real(k, kind=8), k = n, 1, -1)]

    call cpu_time(star)
    call bubble_sort(arr)
    call cpu_time(finish)

    print*, "Tiempo: ", finish - star

    contains

    subroutine bubble_sort(v)
        implicit none

        real(kind=8), intent(inout) :: v(:)
        real(kind=8) :: temp
        integer :: i, j, m
        logical :: swaps

        m = size(v)

        do i = 1, m - 1
            swaps = .false.
            do j = 1, m - i
                if (v(j) .gt. v(j+1)) then
                    temp = v(j)
                    v(j) = v(j+1)
                    v(j+1) = temp
                    swaps = .true.
                endif
            enddo
            if (.not. swaps) exit
        enddo

    end subroutine bubble_sort

end program bubble