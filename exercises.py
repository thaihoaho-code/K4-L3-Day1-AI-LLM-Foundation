import template

def exercise_1():
    prompt_1 = "Hãy kể cho tôi một sự thật thú vị về Việt Nam."

    # def call_openai(
    #     prompt: str,
    #     model: str = OPENAI_MODEL,
    #     temperature: float = 0.7,
    #     top_p: float = 0.9,
    #     max_tokens: int = 256,
    # ) -> tuple[str, float]:
    # temperature 0.0, 0.5, 1.0 và 1.5
        
    response_1, latency_1 = template.call_openai(prompt_1, template.OPENAI_MODEL, temperature=0.0)
    response_2, latency_2 = template.call_openai(prompt_1, template.OPENAI_MODEL, temperature=0.5)
    response_3, latency_3 = template.call_openai(prompt_1, template.OPENAI_MODEL, temperature=1.0)
    response_4, latency_4 = template.call_openai(prompt_1, template.OPENAI_MODEL, temperature=1.5)

    print(f"Prompt: {prompt_1}")
    print(f"Response 1 (temperature=0.0): {response_1} (latency: {latency_1:.2f}s)")
    print(f"Response 2 (temperature=0.5): {response_2} (latency: {latency_2:.2f}s)")
    print(f"Response 3 (temperature=1.0): {response_3} (latency: {latency_3:.2f}s)")
    print(f"Response 4 (temperature=1.5): {response_4} (latency: {latency_4:.2f}s)")
    
def exercise_2_1():
    user_prompt = "Giải thích blockchain là gì?"
    system_prompt_1 = "Bạn là giáo viên tiểu học, giải thích thật đơn giản cho trẻ 8 tuổi."
    system_prompt_2 = "Bạn là chuyên gia tài chính, trả lời chuyên sâu bằng thuật ngữ kỹ thuật."
    response_1, latency_1 = template.chat_with_system_prompt(user_prompt, system_prompt_1)
    response_2, latency_2 = template.chat_with_system_prompt(user_prompt, system_prompt_2)

    print(f"User Prompt: {user_prompt}")
    print(f"Response 1 (Persona: {system_prompt_1}): {response_1} (latency: {latency_1:.2f}s)")
    print(f"Response 2 (Persona: {system_prompt_2}): {response_2} (latency: {latency_2:.2f}s)")


def exercise_2_2():
    # một đoạn văn tiếng Việt ~100 từ.
    text = """
    Trong những năm gần đây, trí tuệ nhân tạo đã được ứng dụng rộng rãi trong giáo dục, tài chính và y tế. Các mô hình như GPT-4o có thể xử lý văn bản, hình ảnh và dữ liệu với tốc độ cao thông qua API. Tuy nhiên, việc triển khai một hệ thống AI thực tế không chỉ phụ thuộc vào độ chính xác của mô hình mà còn liên quan đến chi phí, độ trễ, bảo mật và khả năng mở rộng. Ví dụ, một dịch vụ phục vụ 10.000 người dùng mỗi ngày cần được tối ưu cả về số token, tài nguyên máy chủ và thời gian phản hồi để đảm bảo trải nghiệm ổn định.
    """
    # 124 word
    count_tokens = template.count_tokens(text, model=template.OPENAI_MODEL)
    print(count_tokens)
    # ket qua 165


def main():
    # exercise_1()
    # exercise_2_1()
    exercise_2_2()


if __name__ == "__main__":
    main()