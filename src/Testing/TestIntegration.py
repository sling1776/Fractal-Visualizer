import unittest
import os
import filecmp


'''
Please Note that this test only tests the files in NewPics and Originals. 

If you want to test a new picture, you will have to copy the new picture into the
NewPics Directory and overwrite the old image in there. This will allow you to test 
quickly if the image that was created changed at all. 

If the image is not in the NewPics Directory or in the Originals Directory it will 
simply skip checking them and assume they pass. 
'''
class TestIntegration(unittest.TestCase):
    def test_juliaIntegration(self):
        cwd = os.getcwd()
        self.assertIn("cs1440-lingwall-spencer-assn4", cwd)

        correct = False
        while not correct:
            if not cwd.endswith("assn4"):
                os.chdir("..")
                cwd = os.getcwd()
            else:
                correct = True

        os.chdir("src/Testing/TestDocs/NewPics")

        f = {
            'fulljulia': {
                'centerX': 0.0,
                'centerY': 0.0,
                'axisLength': 4.0,
            },

            'hourglass': {
                'centerX': 0.618,
                'centerY': 0.00,
                'axisLength': 0.017148277367054,
            },

            'lakes': {
                'centerX': -0.339230468501458,
                'centerY': 0.417970758224314,
                'axisLength': 0.164938488846612,
            },

        }

        cwd = os.getcwd()
        print()
        for i in f:
            okay = os.access(f"../Originals/{i}.png", os.F_OK)
            okay2 = os.access(f"{i}.png", os.F_OK)
            if okay and okay2:
                self.assertTrue(filecmp.cmp(cwd + f"\\..\\Originals\\{i}.png", cwd + f"\\{i}.png", shallow=False))
            if not okay2:
                print(f".....{i}.png does not exist in NewPic directory: Skipped check.")
            if not okay:
                print(f".....{i}.png does not exist in Original directory: Skipped check.")


    def test_mandelbrotIntegration(self):
        cwd = os.getcwd()
        self.assertIn("cs1440-lingwall-spencer-assn4", cwd)

        correct = False
        while not correct:
            if not cwd.endswith("assn4"):
                os.chdir("..")
                cwd = os.getcwd()
            else:
                correct = True

        os.chdir("src/Testing/TestDocs/NewPics")

        f = {
            'mandelbrot': {
                'centerX': -0.6,
                'centerY': 0.0,
                'axisLen': 2.5,
            },

            'spiral0': {
                'centerX': -0.761335372924805,
                'centerY': 0.0835704803466797,
                'axisLen': 0.004978179931102462,
            },

            'spiral1': {
                'centerX': -0.747,
                'centerY': 0.1075,
                'axisLen': 0.002,
            },

            'seahorse': {
                'centerX': -0.745,
                'centerY': 0.105,
                'axisLen': 0.01,
            },

            'elephants': {
                'centerX': 0.30820836067024604,
                'centerY': 0.030620936230004017,
                'axisLen': 0.03,
            },

            'leaf': {
                'centerX': -1.543577002,
                'centerY': -0.000058690069,
                'axisLen': 0.000051248888,
            },
        }

        cwd = os.getcwd()
        print()
        for i in f:
            okay = os.access(f"../Originals/{i}.png", os.F_OK)
            okay2 = os.access(f"{i}.png", os.F_OK)
            if okay and okay2:
                self.assertTrue(filecmp.cmp(cwd + f"\\..\\Originals\\{i}.png", cwd + f"\\{i}.png", shallow=False))
            if not okay2:
                print(f".....{i}.png does not exist in NewPic directory: Skipped check.")
            if not okay:
                print(f".....{i}.png does not exist in Original directory: Skipped check.")




if __name__ == '__main__':
    unittest.main()
