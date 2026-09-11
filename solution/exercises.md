# K4 — Ngày 1: Bài Tập & Phản Ánh
## Khám Phá LLM API | Phiếu Thực Hành

**Thời lượng:** 4 tiếng
**Cách làm:** Trả lời từng câu ngay sau khi hoàn thành block tương ứng —
đừng để dồn hết về cuối buổi. Thay dòng `*Câu trả lời của bạn*` bằng câu
trả lời thật (chấm tự động sẽ đếm số câu đã trả lời).

---

## Block 1 — API Cơ Bản (trả lời sau Checkpoint 1)

### Câu 1.1 — Độ nhạy của temperature
Gọi `call_openai` với temperature 0.0, 0.5, 1.0 và 1.5 dùng prompt
**"Hãy kể cho tôi một sự thật thú vị về Việt Nam."**

**Bạn nhận thấy quy luật gì qua bốn phản hồi?** (2–3 câu)
> Khi temperature tăng, phản hồi của mô hình có xu hướng đa dạng và ít xác định hơn. Ở temperature thấp, các câu trả lời khá giống nhau và đều chọn Sơn Đoòng; còn khi tăng lên 1.5, mô hình chuyển sang một chủ đề khác là phở, cho thấy mức độ ngẫu nhiên và sáng tạo tăng.

### Câu 1.2 — Chọn temperature cho sản phẩm
**Bạn sẽ đặt temperature bao nhiêu cho chatbot hỗ trợ khách hàng, và tại sao?**
> Mình sẽ chọn temperature khoảng 0.2–0.3 cho chatbot hỗ trợ khách hàng, vì loại chatbot này cần câu trả lời ổn định, chính xác và nhất quán hơn là quá sáng tạo. Temperature 0.0 và 0.1 có thể quá cứng nhắc, trong khi 0.5 tạo ra nhiều biến thiên hơn mức cần thiết.


### Câu 1.3 — Đánh đổi chi phí
Kịch bản: 10.000 người dùng hoạt động mỗi ngày, mỗi người gọi API 3 lần,
mỗi lần trung bình ~350 token đầu ra.

**Ước tính GPT-4o đắt hơn GPT-4o-mini bao nhiêu lần cho workload này? Nêu một
trường hợp GPT-4o xứng đáng với chi phí và một trường hợp nên dùng mini:**
> Workload không ảnh hưởng đến tỷ lệ chi phí giữa hai model; theo bảng giá đã cho, GPT-4o đắt hơn GPT-4o-mini khoảng 16,7 lần. Với workload trên, chi phí output khoảng $105/ngày cho GPT-4o và $6,3/ngày cho GPT-4o-mini. GPT-4o phù hợp với tác vụ phức tạp cần suy luận và độ chính xác cao, còn GPT-4o-mini phù hợp với tác vụ đơn giản, số lượng lớn như FAQ hoặc phân loại yêu cầu.

> Chi tiết tính toán: 
Ta tính lần lượt:

- Số API calls/ngày: 10,000*3 = 30,000
- Output token/ngày: 30,000*350 = 10,500,000 token
- Tương đương 10,500 đơn vị 1K token

Chi phí output:

$$ \text{GPT-4o} = 10{,}500 \times 0.010 = \$105/\text{ngày} $$ 
$$ \text{GPT-4o-mini} = 10{,}500 \times 0.0006 = \$6.30/\text{ngày} $$

Do đó:

$$ \frac{105}{6.3}\approx 16.67 $$


---

## Block 2 — System Prompt & Token (trả lời sau Checkpoint 2)

### Câu 2.1 — Sức mạnh của persona
Gọi `chat_with_system_prompt` hai lần với cùng câu hỏi
**"Giải thích blockchain là gì?"** nhưng hai system prompt khác nhau:
- "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
- "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."

**Hai phản hồi khác nhau như thế nào (độ dài, từ vựng, ví dụ)? System prompt
ảnh hưởng đến hành vi model ra sao?** (3–4 câu)
> Persona giáo viên tiểu học dùng từ đơn giản, ngắn gọn và ví dụ gần gũi như “cuốn sổ” hay “đoàn tàu”. Ngược lại, persona chuyên gia tài chính trả lời chi tiết hơn và dùng nhiều thuật ngữ kỹ thuật như block, hash, sổ cái phân tán. Điều này cho thấy system prompt định hướng rõ mức độ chuyên sâu, cách dùng từ và cách trình bày của model theo từng đối tượng.


### Câu 2.2 — tiktoken vs đếm từ
Chọn một đoạn văn tiếng Việt ~100 từ. So sánh số token theo `count_tokens`
(tiktoken) với ước lượng `số từ / 0.75` mà Part 1 đã dùng.

**Hai con số chênh nhau bao nhiêu phần trăm? Vì sao tiếng Việt thường tốn
nhiều token hơn tiếng Anh cùng độ dài?**
> Đoạn văn có khoảng 120 từ. Theo công thức ước lượng `số từ / 0.75`, số token dự kiến là khoảng 160 token, trong khi `tiktoken` đếm được 145 token. Hai kết quả chênh nhau khoảng 9,4%, cho thấy công thức trên chỉ là một cách ước lượng và số token thực tế còn phụ thuộc vào cách tokenizer phân tách từ, số, ký hiệu. Tiếng Việt cũng có thể tốn nhiều token hơn tiếng Anh cùng độ dài vì nhiều từ tiếng Việt gồm nhiều âm tiết và các ký tự có dấu có thể được tokenizer chia thành nhiều sub-token.


---

## Block 3 — Streaming & Độ Bền (trả lời sau Checkpoint 3)

### Câu 3.1 — Trải nghiệm người dùng với streaming
**Streaming quan trọng nhất trong trường hợp nào, và khi nào thì
non-streaming lại phù hợp hơn?** (1 đoạn văn)
> Streaming quan trọng nhất khi phản hồi của mô hình dài hoặc mất nhiều thời gian tạo, chẳng hạn chatbot, trợ lý AI hoặc sinh nội dung, vì người dùng có thể thấy kết quả xuất hiện dần thay vì phải chờ toàn bộ phản hồi hoàn tất. Điều này giúp giảm cảm giác chờ đợi và cải thiện trải nghiệm tương tác. Ngược lại, non-streaming phù hợp hơn khi phản hồi ngắn, cần nhận toàn bộ kết quả trước khi xử lý tiếp, hoặc khi ứng dụng cần parse dữ liệu có cấu trúc như JSON sau khi model hoàn thành.

### Câu 3.2 — Vì sao backoff theo cấp số nhân?
**So với delay cố định (ví dụ luôn chờ 1 giây), exponential backoff có lợi
thế gì khi API bị quá tải? Điều gì xảy ra nếu hàng nghìn client cùng retry
với delay cố định giống nhau?**
> Exponential backoff tăng dần thời gian chờ giữa các lần retry, giúp giảm tải cho API và cho server thêm thời gian phục hồi. Nếu hàng nghìn client cùng dùng delay cố định, chúng có thể retry đồng thời và tạo ra một đợt quá tải mới, gọi là “thundering herd”. Vì vậy, exponential backoff thường kết hợp thêm jitter để phân tán thời điểm retry.


---

## Block 4 — Mini-Project (trả lời sau Checkpoint 4)

### Câu 4.1 — Thiết kế persona
**Bạn chọn persona gì cho trợ lý của mình? Viết lại system prompt đó và giải
thích 1–2 lựa chọn từ ngữ quan trọng trong prompt (ví dụ: vì sao yêu cầu
"trả lời ngắn gọn", vì sao chỉ định ngôn ngữ...):**
> Mình chọn persona trợ lý học tập về công nghệ và AI, giúp giải thích kiến thức kỹ thuật dễ hiểu nhưng vẫn chính xác. System prompt: “Bạn là trợ lý học tập chuyên về công nghệ và AI. Hãy trả lời bằng tiếng Việt, ngắn gọn, dễ hiểu, ưu tiên ví dụ thực tế và giữ lại các thuật ngữ tiếng Anh quan trọng khi cần.” Yêu cầu “ngắn gọn, dễ hiểu” giúp người học tập trung vào ý chính, còn việc giữ thuật ngữ tiếng Anh giúp làm quen với từ vựng thường gặp trong tài liệu kỹ thuật.


### Câu 4.2 — Hạn chế & cải thiện
**Trợ lý của bạn hiện có hạn chế lớn nhất là gì (ví dụ: history chỉ 3 lượt,
không có bộ nhớ dài hạn, không kiểm duyệt nội dung...)? Đề xuất một cải
thiện cụ thể và mô tả ngắn cách triển khai:**
> Hạn chế lớn nhất của trợ lý hiện tại là bộ nhớ ngắn hạn. Việc chỉ giữ lại vài lượt hội thoại gần nhất khiến bot dễ mất ngữ cảnh trong các cuộc trò chuyện dài; nhưng nếu đưa toàn bộ lịch sử vào thì sẽ vượt giới hạn context window và tốn kém chi phí token.

> Đề xuất cải thiện: Triển khai bộ nhớ dài hạn bằng kiến trúc RAG (Retrieval-Augmented Generation) kết hợp với cơ sở dữ liệu véc-tơ (Vector Database).

> Cách triển khai: Ứng dụng sẽ dùng mô hình Embedding để chuyển đổi các đoạn chat cũ thành vector và lưu trữ vào Vector DB. Khi người dùng đặt câu hỏi mới, hệ thống sẽ truy vấn top 3-5 đoạn hội thoại trong quá khứ có ý nghĩa liên quan nhất và chèn chúng vào system prompt trước khi gọi API. Giải pháp này giúp trợ lý có trí nhớ lớn hơn, giải quyết đúng trọng tâm mà vẫn tối ưu được chi phí đầu vào.
---

## Danh Sách Kiểm Tra Nộp Bài

- [x] `python grade.py` — xem điểm tự động, mục tiêu ≥ 75/100
- [x] Cả 4 checkpoint pytest đều pass
- [x] Tất cả 9 câu trong file này đã được trả lời
- [x] Đã copy bài làm vào folder `solution/`, push lên fork và dán link trên trang bài Lab ở VLearn trước 23:59 ngày 11/09/2026
