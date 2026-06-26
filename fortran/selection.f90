program selection
    implicit none

    real(kind=8), allocatable :: vector(:)
    integer :: n,k

    n = 10
    vector = [(k, k = n,1,-1)]

    call selection_sort(vector)

    write(*,'(*(F6.2))') vector
    
    contains

    subroutine selection_sort(arr)
        implicit none

        real(kind=8),   intent(inout) :: arr(:)
        real(kind=8) :: key
        integer :: i,pos

        do i = 1, size(arr) - 1
            call compute_min(arr(i:), key, pos)
            arr(i+1 : i+pos-1) = arr(i : i+pos-2)
            arr(i) = key
            
        enddo

    end subroutine selection_sort

    subroutine compute_min(arr,res,pos)
        implicit none

        real(kind=8),   intent(inout) :: arr(:)
        real(kind=8),   intent(out) :: res
        integer,        intent(out) :: pos

        integer :: i

        res = arr(1)
        pos = 1

        do i = 2, size(arr(:))
            if (arr(i) .lt. res) then
                res = arr(i)
                pos = i
            endif
        enddo

    end subroutine compute_min

    
end program selection