program selection
    implicit none

    real(kind=8), allocatable :: arr(:)
    integer :: n,k

    n = 10
    arr = [(real(k, kind=8), k = n, 1, -1)]

    call selection_sort(arr)
    
    contains

    subroutine selection_sort(v)
        implicit none

        real(kind=8),   intent(inout) :: v(:)
        real(kind=8) :: key
        integer :: i,pos

        do i = 1, size(v) - 1
            call compute_min(v(i:), key, pos)
            v(i+1 : i+pos-1) = v(i : i+pos-2)
            v(i) = key
            
        enddo

    end subroutine selection_sort

    subroutine compute_min(v,res,pos)
        implicit none

        real(kind=8),   intent(inout) :: v(:)
        real(kind=8),   intent(out) :: res
        integer,        intent(out) :: pos

        integer :: i

        res = v(1)
        pos = 1

        do i = 2, size(v(:))
            if (v(i) .lt. res) then
                res = v(i)
                pos = i
            endif
        enddo

    end subroutine compute_min

    
end program selection