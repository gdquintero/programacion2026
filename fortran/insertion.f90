program insertion
    implicit none

    real(kind=8), allocatable :: arr(:)
    integer :: k, n

    n = 10
    arr = [(real(k, kind=8), k = n, 1, -1)]

    call insertion_sort(arr)

    write(*,'(*(F6.2))') arr

    contains

    subroutine insertion_sort(v)
        implicit none

        real(kind=8),   intent(inout) :: v(:)
        real(kind=8) :: key
        integer :: i, j

        do i = 2, size(v)
            key = v(i)
            j = i - 1

            do while (j .gt. 0 .and. v(j) .gt. key)
                v(j + 1) = v(j)
                j = j - 1
            enddo

            v(j + 1) = key 

        enddo
    end subroutine insertion_sort
    
end program insertion