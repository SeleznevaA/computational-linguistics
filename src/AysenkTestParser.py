class AysenkTestParser:
    def get_next_question(self):
        """
        Return next question of test

        :rtype String:
        """
        raise NotImplementedError()

    def send_answer(self, answer):
        """
        Send answer of last question to the test-machine

        :param answer:
        """
        raise NotImplementedError()
