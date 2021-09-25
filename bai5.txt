1) git init
Tác dụng : Khởi tạo 1 git repository 1 project mới hoặc đã có.
Cách xài: git init trong thư mục gốc của dự án.
2) git add
Tác dụng: Để đưa một tập tin vào Staging Area
Cách dùng: git add tên_file hoặc muốn thêm hết file của thư mục thì git add all
3) git clone
Tác dụng: Copy 1 git repository từ remote source.
Cách xài: git clone <:clone git url:>
4) git status
Tác dụng: Để check trạng thái của những file bạn đã thay đổi trong thư mục làm việc. VD: Tất cả các thay đổi cuối cùng từ lần commit cuối cùng.
Cách xài: git status trong thư mục làm việc.
5) git add
Tác dụng: Thêm thay đổi đến stage/index trong thư mục làm việc.
Cách xài: git add
6) git commit
Tác dụng: commit nghĩa là một action để Git lưu lại một snapshot của các sự thay đổi trong thư mục làm việc. Và các tập tin, thư mục được thay đổi đã phải nằm trong Staging Area. Mỗi lần commit nó sẽ được lưu lại lịch sử chỉnh sửa của code kèm theo tên và địa chỉ email của người commit. Ngoài ra trong Git bạn cũng có thể khôi phục lại tập tin trong lịch sử commit của nó để chia cho một branch khác, vì vậy bạn sẽ dễ dàng khôi phục lại các thay đổi trước đó.
Cách dùng: git commit -m ”Đây là message, bạn dùng để note những thay đổi để sau này dễ dò lại”
7) git push/git pull
Tác dụng: Push hoặc Pull các thay đổi đến remote. Nếu bạn đã added và committed các thay đổi và bạn muốn đẩy nó lên hoặc remote của bạn đã update và bạn apply tất cả thay đổi đó trên code của mình.
Cách dùng: git pull <:remote:> <:branch:> and git push <:remote:> <:branch:>