program insertion
    implicit none

    real(kind=8), allocatable :: vector(:)
    real(kind=8) :: key
    integer :: i, j, k, n

    n = 10

    vector = [(k, k = n,1,-1)]

    do i = 2, n
        key = vector(i)
        j = i - 1

        do while (j .gt. 0 .and. vector(j) .gt. key)
            vector(j + 1) = vector(j)
            j = j - 1
        enddo

        vector(j + 1) = key 

    enddo

    write(*,'(*(F6.2))') vector
    
end program insertion