def get_bot_response(user_input):
    user_input = user_input.lower()

    if "buồn" in user_input:
        return "Mình hiểu cảm giác đó. Bạn muốn chia sẻ thêm không?"
    elif "cô đơn" in user_input:
        return "Bạn không một mình đâu. Mình luôn ở đây để lắng nghe bạn 💙"
    elif "mệt" in user_input:
        return "Hãy nghỉ ngơi một chút nhé. Thư giãn rất quan trọng!"
    else:
        return "Mình ở đây để nghe bạn. Cứ thoải mái chia sẻ nhé."
